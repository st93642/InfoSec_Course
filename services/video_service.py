"""Video service for VLC playback integration."""

import logging
import platform
import sys
from pathlib import Path
from typing import Optional

try:
    import vlc
    VLC_AVAILABLE = True
except ImportError:
    vlc = None
    VLC_AVAILABLE = False

logger = logging.getLogger(__name__)


class VideoService:
    """
    Service for video playback using VLC.

    This service handles VLC initialization, video loading, playback control,
    and embedding in Qt widgets.

    Attributes:
        instance (vlc.Instance): VLC instance
        player (vlc.MediaPlayer): VLC media player
        is_embedded (bool): Whether video is embedded in a widget
    """

    def __init__(self):
        """
        Initialize the video service.

        Raises:
            RuntimeError: If VLC is not available
        """
        if not VLC_AVAILABLE:
            raise RuntimeError("VLC is not available. Please install python-vlc and VLC.")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.is_embedded = False

        logger.info("Video service initialized with VLC")

    def embed_in_widget(self, widget_win_id: int) -> bool:
        """
        Embed the video player in a Qt widget.

        Args:
            widget_win_id (int): Window ID of the Qt widget

        Returns:
            bool: True if embedding was successful
        """
        try:
            if platform.system() == "Linux":
                self.player.set_xwindow(widget_win_id)
                self.is_embedded = True
                logger.info(f"Embedded video player in widget (win_id: {widget_win_id})")
                return True
            else:
                logger.warning("Video embedding only supported on Linux/X11")
                return False
        except Exception as e:
            logger.error(f"Failed to embed video player: {e}")
            return False

    def load_video(self, video_path: Path) -> bool:
        """
        Load a video file for playback.

        Args:
            video_path (Path): Path to the video file

        Returns:
            bool: True if video was loaded successfully
        """
        try:
            if not video_path.exists():
                logger.error(f"Video file does not exist: {video_path}")
                return False

            media = self.instance.media_new(str(video_path))
            self.player.set_media(media)
            logger.info(f"Loaded video: {video_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to load video {video_path}: {e}")
            return False

    def play(self) -> bool:
        """
        Start video playback.

        Returns:
            bool: True if playback started successfully
        """
        try:
            result = self.player.play()
            if result == 0:  # VLC returns 0 on success
                logger.debug("Started video playback")
                return True
            else:
                logger.error(f"Failed to start playback (VLC error: {result})")
                return False
        except Exception as e:
            logger.error(f"Error starting playback: {e}")
            return False

    def pause(self) -> None:
        """Pause video playback."""
        try:
            self.player.pause()
            logger.debug("Paused video playback")
        except Exception as e:
            logger.error(f"Error pausing playback: {e}")

    def stop(self) -> None:
        """Stop video playback."""
        try:
            self.player.stop()
            logger.debug("Stopped video playback")
        except Exception as e:
            logger.error(f"Error stopping playback: {e}")

    def set_position(self, position: float) -> None:
        """
        Set the playback position.

        Args:
            position (float): Position as a fraction (0.0 to 1.0)
        """
        try:
            self.player.set_position(position)
            logger.debug(f"Set playback position to {position}")
        except Exception as e:
            logger.error(f"Error setting position: {e}")

    def get_position(self) -> float:
        """
        Get the current playback position.

        Returns:
            float: Current position as a fraction (0.0 to 1.0)
        """
        try:
            return self.player.get_position()
        except Exception as e:
            logger.error(f"Error getting position: {e}")
            return 0.0

    def set_volume(self, volume: int) -> None:
        """
        Set the playback volume.

        Args:
            volume (int): Volume level (0-100)
        """
        try:
            self.player.audio_set_volume(volume)
            logger.debug(f"Set volume to {volume}")
        except Exception as e:
            logger.error(f"Error setting volume: {e}")

    def get_length(self) -> int:
        """
        Get the video length in milliseconds.

        Returns:
            int: Video length in milliseconds
        """
        try:
            return self.player.get_length()
        except Exception as e:
            logger.error(f"Error getting length: {e}")
            return 0

    def get_time(self) -> int:
        """
        Get the current playback time in milliseconds.

        Returns:
            int: Current time in milliseconds
        """
        try:
            return self.player.get_time()
        except Exception as e:
            logger.error(f"Error getting time: {e}")
            return 0

    def set_time(self, time_ms: int) -> None:
        """
        Set the playback time.

        Args:
            time_ms (int): Time in milliseconds
        """
        try:
            self.player.set_time(time_ms)
            logger.debug(f"Set playback time to {time_ms}ms")
        except Exception as e:
            logger.error(f"Error setting time: {e}")

    def is_playing(self) -> bool:
        """
        Check if video is currently playing.

        Returns:
            bool: True if video is playing
        """
        try:
            return self.player.is_playing()
        except Exception as e:
            logger.error(f"Error checking play state: {e}")
            return False

    def cleanup(self) -> None:
        """Clean up VLC resources."""
        try:
            if self.player:
                self.player.stop()
                # Note: VLC cleanup is handled by garbage collection
            logger.info("Video service cleaned up")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
