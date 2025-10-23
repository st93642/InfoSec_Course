"""Terminal service for xterm embedding and management."""

import logging
import platform
import subprocess
import sys
from typing import Optional, Tuple

from models.config import ApplicationConfig

logger = logging.getLogger(__name__)


class TerminalService:
    """
    Service for terminal embedding and management.

    This service handles xterm embedding in Qt widgets, geometry management,
    and fallback to external terminals.

    Attributes:
        config (ApplicationConfig): Application configuration
        process (Optional[subprocess.Popen]): The terminal process
        is_embedded (bool): Whether terminal is embedded in a widget
        widget_win_id (Optional[int]): Window ID of the embedding widget
        last_geometry (Optional[str]): Last geometry used for terminal
    """

    def __init__(self, config: ApplicationConfig):
        """
        Initialize the terminal service.

        Args:
            config (ApplicationConfig): Application configuration
        """
        self.config = config
        self.process: Optional[subprocess.Popen] = None
        self.is_embedded = False
        self.widget_win_id: Optional[int] = None
        self.last_geometry: Optional[str] = None

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

            # Set X resources globally for embedded terminal colors
            import subprocess
            xrdb_cmd = ["xrdb", "-merge", "-"]
            xrdb_input = ""
            if self.config.terminal_bg_color:
                xrdb_input += f"xterm*background: {self.config.terminal_bg_color}\n"
            if self.config.terminal_fg_color:
                xrdb_input += f"xterm*foreground: {self.config.terminal_fg_color}\n"
            if self.config.terminal_cursor_color:
                xrdb_input += f"xterm*cursorColor: {self.config.terminal_cursor_color}\n"
            
            if xrdb_input:
                try:
                    subprocess.run(xrdb_cmd, input=xrdb_input, text=True, check=True)
                except (subprocess.SubprocessError, OSError):
                    # xrdb might not be available, continue without it
                    pass

            # Launch xterm embedded in the widget with font settings
            font_size = self.config.terminal_font_size
            cmd = [
                "xterm",
                "-into", str(widget_win_id),
                "-geometry", geometry,
                "-fa", f"Monospace-{font_size}",
                "-fs", str(font_size)
            ]
            
            self.process = subprocess.Popen(cmd)
            self.is_embedded = True
            self.widget_win_id = widget_win_id
            self.last_geometry = geometry

            logger.info(f"Embedded terminal in widget (win_id: {widget_win_id}, geometry: {geometry}, font_size: {font_size})")
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
        if not self.is_embedded or not self.widget_win_id:
            return

        try:
            # Calculate new terminal dimensions
            cols = max(80, width // 8)
            rows = max(24, height // 16)
            new_geometry = f"{cols}x{rows}"

            # Only restart if geometry changed significantly (more than 10 cols/rows difference)
            # or if this is the first time setting geometry
            should_restart = False
            if self.last_geometry is None:
                should_restart = True
            else:
                old_cols, old_rows = map(int, self.last_geometry.split('x'))
                if abs(cols - old_cols) >= 10 or abs(rows - old_rows) >= 5:
                    should_restart = True

            if should_restart:
                logger.info(f"Restarting terminal with new geometry: {new_geometry} (was {self.last_geometry})")
                self.last_geometry = new_geometry

                # Restart terminal with new geometry
                if self.process and self.is_running():
                    self.process.terminate()
                    try:
                        self.process.wait(timeout=1.0)
                    except subprocess.TimeoutExpired:
                        self.process.kill()
                        self.process.wait()

                # Set X resources globally for embedded terminal colors
                xrdb_cmd = ["xrdb", "-merge", "-"]
                xrdb_input = ""
                if self.config.terminal_bg_color:
                    xrdb_input += f"xterm*background: {self.config.terminal_bg_color}\n"
                if self.config.terminal_fg_color:
                    xrdb_input += f"xterm*foreground: {self.config.terminal_fg_color}\n"
                if self.config.terminal_cursor_color:
                    xrdb_input += f"xterm*cursorColor: {self.config.terminal_cursor_color}\n"
                
                if xrdb_input:
                    try:
                        subprocess.run(xrdb_cmd, input=xrdb_input, text=True, check=True)
                    except (subprocess.SubprocessError, OSError):
                        # xrdb might not be available, continue without it
                        pass

                # Launch with new geometry
                font_size = self.config.terminal_font_size
                cmd = [
                    "xterm",
                    "-into", str(self.widget_win_id),
                    "-geometry", new_geometry,
                    "-fa", f"Monospace-{font_size}",
                    "-fs", str(font_size)
                ]
                
                self.process = subprocess.Popen(cmd)

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
                self.last_geometry = None

    def __del__(self):
        """Destructor to ensure cleanup."""
        self.cleanup()
