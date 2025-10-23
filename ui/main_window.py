"""Main window for the Video Terminal application."""

import logging
import threading
from typing import Optional

from PyQt5 import QtCore, QtWidgets

from models.config import ApplicationConfig
from models.release_video import ReleaseVideo
from services.download_service import DownloadService
from services.github_service import GitHubService
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

    def __init__(self, config: ApplicationConfig, selected_tag: Optional[str] = None):
        """
        Initialize the main window.

        Args:
            config (ApplicationConfig): Application configuration
            selected_tag (Optional[str]): Pre-selected release tag
        """
        super().__init__()

        self.config = config
        self.selected_tag = selected_tag

        # Initialize services
        self.github_service = GitHubService(config)
        self.download_service = DownloadService(config)
        self.video_service = VideoService()
        self.terminal_service = TerminalService()

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
        lower_layout.addWidget(self.playlist_widget, 1)  # Equal stretch

        # Terminal widget (right side of lower section)
        self.terminal_widget = TerminalWidget()
        self.terminal_widget.set_terminal_service(self.terminal_service)
        lower_layout.addWidget(self.terminal_widget, 1)  # Equal stretch

        main_layout.addWidget(lower_section, 2)  # Lower section

        # Status section at bottom
        status_section = QtWidgets.QWidget()
        status_layout = QtWidgets.QHBoxLayout(status_section)

        self.status_label = QtWidgets.QLabel("Ready")
        self.status_label.setStyleSheet("color: white;")
        status_layout.addWidget(self.status_label)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(False)
        status_layout.addWidget(self.progress_bar)

        main_layout.addWidget(status_section)

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

        # Update text content
        content = video.get_content_text()
        self.text_widget.set_content(content)

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

        try:
            self.controls_widget.show_download_progress(True)
            self.status_label.setText(f"Downloading {video.asset_name}...")

            # Check if already cached
            cache_path = self.download_service.get_cached_asset_path(video.asset_name)
            if not self.download_service.is_asset_cached(video.asset_name):
                # Download in background thread
                threading.Thread(
                    target=self._download_video,
                    args=(video.asset_url, cache_path, download_progress, download_complete),
                    daemon=True
                ).start()
            else:
                # Already cached, play directly
                self.controls_widget.show_download_progress(False)
                self._play_video(video)

        except Exception as e:
            logger.error(f"Error initiating download: {e}")
            self.status_label.setText(f"Error: {e}")
            self.controls_widget.show_download_progress(False)

    def _download_video(
        self,
        url: str,
        destination_path,
        progress_callback,
        completion_callback
    ) -> None:
        """
        Download video in background thread.

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
            logger.error(f"Download failed: {e}")
            QtCore.QMetaObject.invokeMethod(
                self, "_on_download_error",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(str, str(e))
            )

    @QtCore.pyqtSlot(object)
    def _on_download_complete(self, completion_callback) -> None:
        """Handle download completion in main thread."""
        completion_callback()

    @QtCore.pyqtSlot(str)
    def _on_download_error(self, error_message: str) -> None:
        """Handle download error in main thread."""
        self.status_label.setText(f"Download error: {error_message}")
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
                self.status_label.setText(f"Playing: {video.display_name}")
                logger.info(f"Started playing: {video.display_name}")
            else:
                self.status_label.setText("Failed to load video")
                logger.error("Failed to load video for playback")

        except Exception as e:
            logger.error(f"Error playing video: {e}")
            self.status_label.setText(f"Playback error: {e}")

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

    def load_videos(self) -> None:
        """Load videos from GitHub releases."""
        def load_videos_thread():
            try:
                QtCore.QMetaObject.invokeMethod(
                    self, "_set_loading_state",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(bool, True)
                )

                videos = self.github_service.fetch_releases(self.selected_tag)

                QtCore.QMetaObject.invokeMethod(
                    self, "_set_loading_state",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(bool, False)
                )

                for video in videos:
                    QtCore.QMetaObject.invokeMethod(
                        self, "_add_video_to_playlist",
                        QtCore.Qt.QueuedConnection,
                        QtCore.Q_ARG(object, video)
                    )

                QtCore.QMetaObject.invokeMethod(
                    self, "_set_status_text",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(str, f"Loaded {len(videos)} videos")
                )

            except Exception as e:
                logger.error(f"Error loading videos: {e}")
                QtCore.QMetaObject.invokeMethod(
                    self, "_set_status_text",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(str, f"Error loading videos: {e}")
                )
                QtCore.QMetaObject.invokeMethod(
                    self, "_set_loading_state",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(bool, False)
                )

        # Start loading in background thread
        threading.Thread(target=load_videos_thread, daemon=True).start()

    @QtCore.pyqtSlot(bool)
    def _set_loading_state(self, loading: bool) -> None:
        """Set the loading state of the progress bar."""
        self.progress_bar.setVisible(loading)
        if loading:
            self.progress_bar.setRange(0, 0)  # Indeterminate progress

    @QtCore.pyqtSlot(object)
    def _add_video_to_playlist(self, video: ReleaseVideo) -> None:
        """Add a video to the playlist in the main thread."""
        self.playlist_widget.add_video(video)

    @QtCore.pyqtSlot(str)
    def _set_status_text(self, text: str) -> None:
        """Set the status text in the main thread."""
        self.status_label.setText(text)

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
