"""Terminal widget for embedding xterm or other terminals."""

import logging
from typing import Optional

from PyQt5 import QtCore, QtGui, QtWidgets

from services.terminal_service import TerminalService

logger = logging.getLogger(__name__)


class TerminalWidget(QtWidgets.QWidget):
    """
    Widget for embedding a terminal.

    This widget provides a container for terminal embedding and handles
    resize events to update terminal geometry.

    Attributes:
        terminal_service (Optional[TerminalService]): The terminal service instance
    """

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        """
        Initialize the terminal widget.

        Args:
            parent (Optional[QWidget]): Parent widget
        """
        super().__init__(parent)
        self.terminal_service: Optional[TerminalService] = None

        # Configure appearance
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                border: 1px solid #333;
            }
        """)

        # Set size policy
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(400, 200)

        # Set up layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def set_terminal_service(self, terminal_service: TerminalService) -> None:
        """
        Set the terminal service for this widget.

        Args:
            terminal_service (TerminalService): The terminal service instance
        """
        self.terminal_service = terminal_service

        # Attempt to embed terminal
        if not self._embed_terminal():
            self._show_fallback_message()

    def _embed_terminal(self) -> bool:
        """
        Attempt to embed a terminal in this widget.

        Returns:
            bool: True if embedding was successful
        """
        if not self.terminal_service:
            return False

        try:
            # Calculate initial geometry
            size = self.size()
            geometry = self.terminal_service.get_recommended_geometry(size.width(), size.height())

            # Embed terminal
            success = self.terminal_service.embed_in_widget(int(self.winId()), geometry)

            if success:
                logger.info("Terminal embedded successfully")
            else:
                logger.warning("Terminal embedding failed, will show fallback")

            return success

        except Exception as e:
            logger.error(f"Error embedding terminal: {e}")
            return False

    def _show_fallback_message(self) -> None:
        """Show a fallback message when terminal embedding fails."""
        label = QtWidgets.QLabel("Terminal embedding not available.\nClick to open external terminal.")
        label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: #333;
                padding: 20px;
                border-radius: 5px;
                font-size: 12pt;
                text-align: center;
            }
        """)
        label.setAlignment(QtCore.Qt.AlignCenter)

        # Make label clickable to launch external terminal
        label.mousePressEvent = self._launch_external_terminal

        # Clear existing layout and add label
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(label)

    def _launch_external_terminal(self, event: QtGui.QMouseEvent) -> None:
        """
        Launch an external terminal when fallback label is clicked.

        Args:
            event (QMouseEvent): The mouse event
        """
        if self.terminal_service:
            success = self.terminal_service.launch_external_terminal()
            if success:
                logger.info("Launched external terminal from fallback")
            else:
                logger.error("Failed to launch external terminal")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Handle widget resize events.

        Args:
            event (QResizeEvent): The resize event
        """
        super().resizeEvent(event)

        # Update terminal geometry if embedded
        if self.terminal_service and self.terminal_service.is_embedded:
            size = self.size()
            self.terminal_service.update_geometry(size.width(), size.height())

    def minimumSizeHint(self) -> QtCore.QSize:
        """
        Get the minimum size hint for the widget.

        Returns:
            QSize: Minimum recommended size
        """
        return QtCore.QSize(400, 200)

    def sizeHint(self) -> QtCore.QSize:
        """
        Get the preferred size hint for the widget.

        Returns:
            QSize: Preferred size
        """
        return QtCore.QSize(600, 400)

    def cleanup(self) -> None:
        """Clean up the terminal service."""
        if self.terminal_service:
            self.terminal_service.cleanup()
