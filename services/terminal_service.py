"""Terminal service for xterm embedding and management."""

import logging
import platform
import subprocess
import sys
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class TerminalService:
    """
    Service for terminal embedding and management.

    This service handles xterm embedding in Qt widgets, geometry management,
    and fallback to external terminals.

    Attributes:
        process (Optional[subprocess.Popen]): The terminal process
        is_embedded (bool): Whether terminal is embedded in a widget
        widget_win_id (Optional[int]): Window ID of the embedding widget
    """

    def __init__(self):
        """Initialize the terminal service."""
        self.process: Optional[subprocess.Popen] = None
        self.is_embedded = False
        self.widget_win_id: Optional[int] = None

    def embed_in_widget(self, widget_win_id: int, geometry: Optional[str] = None) -> bool:
        """
        Embed a terminal in a Qt widget.

        Args:
            widget_win_id (int): Window ID of the Qt widget
            geometry (Optional[str]): Terminal geometry (e.g., "80x24")

        Returns:
            bool: True if embedding was successful
        """
        if platform.system() != "Linux":
            logger.warning("Terminal embedding only supported on Linux")
            return False

        try:
            # Kill any existing terminal
            self.cleanup()

            # Set default geometry if not provided
            if geometry is None:
                geometry = "80x24"

            # Launch xterm embedded in the widget
            cmd = ["xterm", "-into", str(widget_win_id), "-geometry", geometry]
            self.process = subprocess.Popen(cmd)
            self.is_embedded = True
            self.widget_win_id = widget_win_id

            logger.info(f"Embedded terminal in widget (win_id: {widget_win_id}, geometry: {geometry})")
            return True

        except (subprocess.SubprocessError, OSError) as e:
            logger.error(f"Failed to embed terminal: {e}")
            self.is_embedded = False
            return False

    def launch_external_terminal(self) -> bool:
        """
        Launch an external terminal window.

        Returns:
            bool: True if terminal was launched successfully
        """
        try:
            # Kill any existing embedded terminal
            self.cleanup()

            # Launch external xterm
            self.process = subprocess.Popen(["xterm"])
            self.is_embedded = False

            logger.info("Launched external terminal")
            return True

        except (subprocess.SubprocessError, OSError) as e:
            logger.error(f"Failed to launch external terminal: {e}")
            return False

    def update_geometry(self, width: int, height: int) -> None:
        """
        Update the terminal geometry based on widget size.

        Args:
            width (int): Widget width in pixels
            height (int): Widget height in pixels
        """
        if not self.is_embedded or not self.process:
            return

        try:
            # Calculate terminal dimensions
            # Approximate: 8 pixels per character width, 16 pixels per line height
            cols = max(80, width // 8)
            rows = max(24, height // 16)

            # Note: xterm doesn't support dynamic geometry changes after launch
            # This is a placeholder for future enhancements
            logger.debug(f"Calculated terminal geometry: {cols}x{rows} for widget {width}x{height}")

        except Exception as e:
            logger.error(f"Error updating terminal geometry: {e}")

    def get_recommended_geometry(self, width: int, height: int) -> str:
        """
        Get recommended terminal geometry for given widget dimensions.

        Args:
            width (int): Widget width in pixels
            height (int): Widget height in pixels

        Returns:
            str: Geometry string (e.g., "80x24")
        """
        cols = max(80, width // 8)
        rows = max(24, height // 16)
        return f"{cols}x{rows}"

    def is_running(self) -> bool:
        """
        Check if the terminal process is running.

        Returns:
            bool: True if terminal is running
        """
        if not self.process:
            return False

        return self.process.poll() is None

    def send_signal(self, signal: int) -> None:
        """
        Send a signal to the terminal process.

        Args:
            signal (int): Signal number to send
        """
        if self.process and self.is_running():
            try:
                self.process.send_signal(signal)
                logger.debug(f"Sent signal {signal} to terminal")
            except OSError as e:
                logger.error(f"Failed to send signal {signal}: {e}")

    def cleanup(self) -> None:
        """Clean up the terminal process."""
        if self.process:
            try:
                if self.is_running():
                    self.process.terminate()
                    # Give it a moment to terminate gracefully
                    try:
                        self.process.wait(timeout=2.0)
                    except subprocess.TimeoutExpired:
                        # Force kill if it doesn't terminate
                        self.process.kill()
                        self.process.wait()

                logger.info("Terminal process cleaned up")
            except Exception as e:
                logger.error(f"Error during terminal cleanup: {e}")
            finally:
                self.process = None
                self.is_embedded = False
                self.widget_win_id = None

    def __del__(self):
        """Destructor to ensure cleanup."""
        self.cleanup()
