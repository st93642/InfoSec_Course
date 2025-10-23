"""Video widget for displaying video content."""

import logging
from typing import Optional

from PyQt5 import QtCore, QtGui, QtWidgets

from services.video_service import VideoService

logger = logging.getLogger(__name__)


class VideoWidget(QtWidgets.QFrame):
    """
    Widget for displaying video content using VLC.

    This widget provides a surface for VLC video embedding and handles
    the integration between Qt and VLC.

    Attributes:
        video_service (Optional[VideoService]): The video service instance
    """

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        """
        Initialize the video widget.

        Args:
            parent (Optional[QWidget]): Parent widget
        """
        super().__init__(parent)
        self.video_service: Optional[VideoService] = None

        # Set up the widget appearance
        self.setFrameStyle(QtWidgets.QFrame.Box)
        self.setStyleSheet("background-color: black;")
        self.setMinimumSize(320, 240)

        # Set size policy to expand
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def set_video_service(self, video_service: VideoService) -> None:
        """
        Set the video service for this widget.

        Args:
            video_service (VideoService): The video service instance
        """
        self.video_service = video_service

        # Embed VLC in this widget
        if not video_service.embed_in_widget(int(self.winId())):
            logger.warning("Failed to embed video in widget")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Handle widget resize events.

        Args:
            event (QResizeEvent): The resize event
        """
        super().resizeEvent(event)

        # Update video display if embedded
        if self.video_service and self.video_service.is_embedded:
            # VLC handles resize automatically when embedded
            pass

    def minimumSizeHint(self) -> QtCore.QSize:
        """
        Get the minimum size hint for the widget.

        Returns:
            QSize: Minimum recommended size
        """
        return QtCore.QSize(320, 240)

    def sizeHint(self) -> QtCore.QSize:
        """
        Get the preferred size hint for the widget.

        Returns:
            QSize: Preferred size
        """
        return QtCore.QSize(640, 480)
