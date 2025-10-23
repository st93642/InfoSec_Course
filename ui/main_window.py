"""Main window for the Video Terminal application."""

import logging
import threading
from typing import Optional

from PyQt5 import QtCore, QtWidgets

from models.config import ApplicationConfig
from models.release_video import ReleaseVideo
from models.video_library import VideoLibrary
from services.download_service import DownloadService
from services.terminal_service import TerminalService
from services.video_service import VideoService
from .playback_controls_widget import PlaybackControlsWidget
from .playlist_widget import PlaylistWidget
from .terminal_widget import TerminalWidget
from .text_content_widget import TextContentWidget
from .video_widget import VideoWidget

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    """
    Main application window for the Video Terminal.

    This window organizes all UI components in a 4-pane layout:
    - Upper-left: Video display
    - Upper-right: Text content
    - Lower-left: Playlist
    - Lower-right: Terminal

    Attributes:
        config (ApplicationConfig): Application configuration
        github_service (GitHubService): GitHub API service
        download_service (DownloadService): Download service
        video_service (VideoService): Video playback service
        terminal_service (TerminalService): Terminal service
    """

    def __init__(self, config: ApplicationConfig):
        """
        Initialize the main window.

        Args:
            config (ApplicationConfig): Application configuration
        """
        super().__init__()

        self.config = config
        self.selected_tag = None  # Will be set when video is selected from tree

        # Initialize services
        self.github_service = None  # No longer needed with static data
        self.download_service = DownloadService(config)
        self.video_service = VideoService()
        self.terminal_service = TerminalService(config)

        # Track current playback and background prefetching
        self.current_video: Optional[ReleaseVideo] = None
        self._prefetch_lock = threading.Lock()
        self._prefetching_asset: Optional[str] = None

        # Setup UI
        self._setup_ui()
        self._connect_signals()

        # Setup window properties
        self.setWindowTitle("Video Terminal - Pilot")
        self.resize(1200, 800)
        self.setStyleSheet("QMainWindow { background-color: black; }")

        logger.info("Main window initialized")

    def _setup_ui(self) -> None:
        """Set up the user interface."""
        # Create central widget and main layout
        central_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # Create upper section (video + text)
        upper_section = QtWidgets.QWidget()
        upper_layout = QtWidgets.QHBoxLayout(upper_section)

        # Video widget (left side of upper section)
        self.video_widget = VideoWidget()
        self.video_widget.set_video_service(self.video_service)
        upper_layout.addWidget(self.video_widget, 2)  # Stretch factor 2

        # Text content widget (right side of upper section)
        self.text_widget = TextContentWidget()
        upper_layout.addWidget(self.text_widget, 1)  # Stretch factor 1

        main_layout.addWidget(upper_section, 3)  # Upper section gets more space

        # Playback controls
        self.controls_widget = PlaybackControlsWidget()
        main_layout.addWidget(self.controls_widget)

        # Create lower section (playlist + terminal)
        lower_section = QtWidgets.QWidget()
        lower_layout = QtWidgets.QHBoxLayout(lower_section)

        # Playlist widget (left side of lower section)
        self.playlist_widget = PlaylistWidget()
        lower_layout.addWidget(self.playlist_widget, 1)  # Stretch factor 1

        # Terminal widget (right side of lower section)
        self.terminal_widget = TerminalWidget()
        self.terminal_widget.set_terminal_service(self.terminal_service)
        lower_layout.addWidget(self.terminal_widget, 2)  # Stretch factor 2 (wider than playlist)

        main_layout.addWidget(lower_section, 2)  # Lower section

        self.setCentralWidget(central_widget)

        # Set up update timer for video position
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self._update_video_position)
        self.update_timer.start(1000)  # Update every second

    def _connect_signals(self) -> None:
        """Connect all signal handlers."""
        # Playlist selection
        self.playlist_widget.video_selected.connect(self._on_video_selected)

        # Playback controls
        self.controls_widget.play_requested.connect(self._on_play_requested)
        self.controls_widget.pause_requested.connect(self._on_pause_requested)
        self.controls_widget.seek_requested.connect(self._on_seek_requested)
        self.controls_widget.volume_changed.connect(self._on_volume_changed)

    def _on_video_selected(self, video: ReleaseVideo) -> None:
        """
        Handle video selection from playlist.

        Args:
            video (ReleaseVideo): The selected video
        """
        logger.info(f"Video selected: {video.display_name}")

        # Update selected tag for this video
        self.selected_tag = video.tag
        self.current_video = video

        # Start download and playback
        self._download_and_play_video(video)

    def _download_and_play_video(self, video: ReleaseVideo) -> None:
        """
        Download and play the selected video.

        Args:
            video (ReleaseVideo): Video to download and play
        """
        def download_progress(downloaded: int, total: int) -> None:
            # Update progress in main thread
            QtCore.QMetaObject.invokeMethod(
                self, "_update_download_progress",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(int, downloaded),
                QtCore.Q_ARG(int, total)
            )

        def download_complete() -> None:
            self.controls_widget.show_download_progress(False)
            self._play_video(video)

        def text_download_complete() -> None:
            # Load and display text content
            self._load_and_display_text_content(video)

        try:
            self.controls_widget.show_download_progress(True)
            logger.info(f"Downloading {video.asset_name}...")

            # Check if video is already cached
            cache_path = self.download_service.get_cached_asset_path(video.asset_name)
            if not self.download_service.is_asset_cached(video.asset_name):
                # Download video in background thread
                threading.Thread(
                    target=self._download_video,
                    args=(video.asset_url, cache_path, download_progress, download_complete),
                    daemon=True
                ).start()
            else:
                # Video already cached, play directly
                download_complete()

            # Download text file if available
            if video.text_url:
                # Extract text filename from URL (e.g., "1.Area.of.use.Linux.txt")
                text_filename = video.text_url.split('/')[-1]
                text_cache_path = self.download_service.get_cached_asset_path(text_filename)
                if not self.download_service.is_asset_cached(text_filename):
                    # Download text in background thread
                    threading.Thread(
                        target=self._download_text_file,
                        args=(video.text_url, text_cache_path, text_download_complete),
                        daemon=True
                    ).start()
                else:
                    # Text already cached, load directly
                    text_download_complete()
            else:
                # No text file available, use static description
                self._load_and_display_text_content(video)

        except Exception as e:
            logger.error(f"Error initiating download: {e}")
            self.controls_widget.show_download_progress(False)

    def _download_video(
        self,
        url: str,
        destination_path: str,
        progress_callback,
        completion_callback
    ) -> None:
        """
        Download video file in background thread.

        Args:
            url (str): Download URL
            destination_path: Path to save file
            progress_callback: Function to call with progress updates
            completion_callback: Function to call when download completes
        """
        try:
            self.download_service.download_asset(url, destination_path, progress_callback)
            # Update UI in main thread
            QtCore.QMetaObject.invokeMethod(
                self, "_on_download_complete",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(object, completion_callback)
            )
        except Exception as e:
            logger.error(f"Video download failed: {e}")
            QtCore.QMetaObject.invokeMethod(
                self, "_on_download_error",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(str, str(e))
            )

    def _download_text_file(
        self,
        url: str,
        destination_path: str,
        completion_callback
    ) -> None:
        """
        Download text file in background thread.

        Args:
            url (str): Download URL
            destination_path: Path to save file
            completion_callback: Function to call when download completes
        """
        try:
            self.download_service.download_asset(url, destination_path, None)
            # Update UI in main thread
            QtCore.QMetaObject.invokeMethod(
                self, "_on_text_download_complete",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(object, completion_callback)
            )
        except Exception as e:
            logger.error(f"Text download failed: {e}")
            QtCore.QMetaObject.invokeMethod(
                self, "_on_text_download_error",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(str, str(e))
            )

    @QtCore.pyqtSlot(object)
    def _on_text_download_complete(self, completion_callback) -> None:
        """Handle text download completion in main thread."""
        completion_callback()

    @QtCore.pyqtSlot(str)
    def _on_text_download_error(self, error_message: str) -> None:
        """Handle text download error in main thread."""
        logger.error(f"Text download error: {error_message}")

    def _load_and_display_text_content(self, video: ReleaseVideo) -> None:
        """
        Load and display text content for the video.

        Args:
            video (ReleaseVideo): Video to load text content for
        """
        try:
            content = None

            # Check if we have a text URL to load from
            if video.text_url:
                # Extract text filename from URL (e.g., "1.1.Principles.of.Building.Networks.txt")
                text_filename = video.text_url.split('/')[-1]
                text_cache_path = self.download_service.get_cached_asset_path(text_filename)

                # Download text file if not cached
                if not self.download_service.is_asset_cached(text_filename):
                    try:
                        logger.info(f"Downloading text content from {video.text_url}")
                        self.download_service.download_asset(video.text_url, text_cache_path)
                    except Exception as e:
                        logger.warning(f"Failed to download text content: {e}")
                        content = "Text content not available (download failed)"
                else:
                    logger.info(f"Using cached text content: {text_cache_path}")

                # Try to read the text file with multiple encodings
                if content is None:
                    try:
                        # Try UTF-8 first
                        with open(text_cache_path, 'r', encoding='utf-8') as f:
                            content = f.read().strip()
                    except UnicodeDecodeError:
                        try:
                            # Try Windows-1252 encoding
                            with open(text_cache_path, 'r', encoding='windows-1252') as f:
                                content = f.read().strip()
                        except UnicodeDecodeError:
                            try:
                                # Try latin-1 as fallback
                                with open(text_cache_path, 'r', encoding='latin-1') as f:
                                    content = f.read().strip()
                            except UnicodeDecodeError:
                                # If all encodings fail, show error message
                                content = "Error: Unable to decode text file (unsupported encoding)"

            # Fall back to static description if no text URL or if text loading failed
            if not content:
                if video.text_url:
                    content = "No text content available for this video"
                else:
                    content = video.description or "No description available"

            logger.info(f"Setting text content: '{content[:100]}...' (length: {len(content)})")
            self.text_widget.set_content(content)

        except Exception as e:
            logger.error(f"Error loading text content: {e}")
            self.text_widget.set_content("Error loading text content")

    @QtCore.pyqtSlot(object)
    def _on_download_complete(self, completion_callback) -> None:
        """Handle download completion in main thread."""
        completion_callback()

    @QtCore.pyqtSlot(str)
    def _on_download_error(self, error_message: str) -> None:
        """Handle download error in main thread."""
        logger.error(f"Download error: {error_message}")
        self.controls_widget.show_download_progress(False)

    @QtCore.pyqtSlot(int, int)
    def _update_download_progress(self, downloaded: int, total: int) -> None:
        """Update download progress in main thread."""
        self.controls_widget.set_download_progress(downloaded, total)

    def _play_video(self, video: ReleaseVideo) -> None:
        """
        Play the downloaded video.

        Args:
            video (ReleaseVideo): Video to play
        """
        try:
            cache_path = self.download_service.get_cached_asset_path(video.asset_name)

            if self.video_service.load_video(cache_path):
                self.video_service.play()
                self.controls_widget.enable_controls(True)
                self.controls_widget.reset_position()
                logger.info(f"Playing: {video.display_name}")
                self.current_video = video
                self._prefetch_next_video(video)
            else:
                logger.error("Failed to load video for playback")

        except Exception as e:
            logger.error(f"Error playing video: {e}")

    def _on_play_requested(self) -> None:
        """Handle play button press."""
        if self.video_service.play():
            self.controls_widget.set_playing(True)
        else:
            logger.error("Failed to start playback")

    def _on_pause_requested(self) -> None:
        """Handle pause button press."""
        self.video_service.pause()
        self.controls_widget.set_playing(False)

    def _on_seek_requested(self, position: float) -> None:
        """
        Handle seek position change.

        Args:
            position (float): Seek position (0.0-1.0)
        """
        self.video_service.set_position(position)

    def _on_volume_changed(self, volume: int) -> None:
        """
        Handle volume change.

        Args:
            volume (int): Volume level (0-100)
        """
        self.video_service.set_volume(volume)

    def _update_video_position(self) -> None:
        """Update the video position display."""
        if self.video_service.is_playing():
            position = self.video_service.get_position()
            self.controls_widget.set_position(position)

    def _prefetch_next_video(self, current_video: ReleaseVideo) -> None:
        """Start a background download for the next video if not cached."""
        try:
            next_video = self.playlist_widget.get_next_video(current_video)
        except Exception as exc:
            logger.error(f"Unable to determine next video: {exc}")
            return

        if not next_video:
            return

        asset_name = next_video.asset_name
        if self.download_service.is_asset_cached(asset_name):
            logger.debug(f"Next video already cached: {asset_name}")
            return

        with self._prefetch_lock:
            if self._prefetching_asset is not None:
                # Already downloading something else in the background
                if self._prefetching_asset == asset_name:
                    logger.debug(f"Prefetch already in progress for {asset_name}")
                else:
                    logger.debug("Background prefetch in progress; skipping new request")
                return
            self._prefetching_asset = asset_name

        cache_path = self.download_service.get_cached_asset_path(asset_name)

        def _prefetch_worker() -> None:
            try:
                logger.info(f"Prefetching next video: {next_video.display_name}")
                self.download_service.download_asset(next_video.asset_url, cache_path)
                logger.info(f"Prefetch complete: {next_video.display_name}")
            except Exception as e:
                logger.warning(f"Failed to prefetch video {asset_name}: {e}")
            finally:
                with self._prefetch_lock:
                    self._prefetching_asset = None

        threading.Thread(target=_prefetch_worker, daemon=True).start()

    def load_all_videos_tree(self) -> None:
        """Load all videos organized in a concise tree: 13 main folders (releases) with sections underneath."""
        try:
            # Get all releases
            releases = VideoLibrary.get_releases()
            
            # Clear existing playlist
            self.playlist_widget.clear_playlist()
            
            # Add videos organized by release (top-level) and section (nested)
            total_videos = 0
            
            # Sort releases numerically (oldest first)
            def version_key(version):
                return tuple(int(x) for x in version.split('.'))
            
            for release_tag in sorted(releases, key=version_key):
                # Add release as MAIN top-level folder with title and count
                release_title = VideoLibrary.get_release_title(release_tag)
                sections = VideoLibrary.get_release_sections(release_tag)
                section_count = len(sections)
                video_count = sum(len(v) for v in sections.values())
                release_item = self.playlist_widget.add_category(f"{release_title}")
                
                # Sort sections within release
                for section_key in sorted(sections.keys(), key=self._sort_section_key):
                    # Add section as subcategory with count
                    section_name = VideoLibrary.get_section_name(release_tag, section_key)
                    section_videos = sections[section_key]
                    section_item = self.playlist_widget.add_subcategory(
                        release_item, 
                        f"{section_name}"
                    )
                    
                    # Add videos under this section (sorted)
                    for full_name in sorted(section_videos, key=self._sort_video_key):
                        video_data = VideoLibrary.get_video_info(full_name)
                        if video_data:
                            # Create concise display name
                            display_name = self._create_concise_video_name(video_data)
                            
                            video = ReleaseVideo(
                                tag=video_data["release_tag"],
                                body="",
                                asset_name=video_data["name"],
                                asset_url=video_data["url"],
                                text_url=video_data.get("text_url"),
                                description=video_data["description"]
                            )
                            video._display_name = display_name
                            self.playlist_widget.add_video_to_category(section_item, video)
                            total_videos += 1
            
            logger.info(f"Loaded {total_videos} videos in concise tree structure from {len(releases)} main folders")
            
        except Exception as e:
            logger.error(f"Error loading videos tree: {e}")
    
    @staticmethod
    def _sort_section_key(section_key: str) -> tuple:
        """Extract numeric part from section key for proper sorting."""
        import re
        match = re.search(r'(\d+)', section_key)
        if match:
            return (int(match.group(1)),)
        return (999,)
    
    @staticmethod
    def _sort_video_key(video_name: str) -> tuple:
        """Extract numeric parts from video name for proper sorting."""
        import re
        numbers = re.findall(r'\d+', video_name)
        return tuple(int(n) for n in numbers) if numbers else (999,)
    
    @staticmethod
    def _create_concise_video_name(video_data: dict) -> str:
        """Create a concise video name from metadata."""
        description = video_data.get("description", "")
        
        if not description:
            # Fallback to filename-based extraction
            clean_name = VideoLibrary.get_display_name_without_extension(video_data["name"])
            return clean_name.replace(".", " ")
        
        # Extract and format description
        # Description format: "13 1 1 Git Introduction" -> "1.1 Git Introduction"
        parts = description.split()
        
        # Find numeric prefix and text
        numbering_parts = []
        text_start_idx = 0
        
        for i, part in enumerate(parts):
            if part.isdigit():
                numbering_parts.append(part)
            else:
                text_start_idx = i
                break
        
        # Create display name
        if numbering_parts:
            # Skip first number (release) for display, use rest as numbering
            if len(numbering_parts) > 1:
                display_numbers = '.'.join(numbering_parts[1:])
                text_part = ' '.join(parts[text_start_idx:])
                return f"{display_numbers} {text_part}".strip()
            else:
                text_part = ' '.join(parts[text_start_idx:])
                return text_part.strip()
        
        return description

    def closeEvent(self, event) -> None:
        """
        Handle window close event.

        Args:
            event: Close event
        """
        logger.info("Main window closing")

        # Clean up services
        if self.video_service:
            self.video_service.cleanup()
        if self.terminal_widget:
            self.terminal_widget.cleanup()

        super().closeEvent(event)
