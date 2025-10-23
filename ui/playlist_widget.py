"""Playlist widget for displaying and selecting video items."""

import logging
from typing import Callable, List, Optional

from PyQt5 import QtCore, QtGui, QtWidgets

from models.release_video import ReleaseVideo

logger = logging.getLogger(__name__)


class PlaylistWidget(QtWidgets.QListWidget):
    """
    Widget for displaying a playlist of video items.

    This widget shows available videos and allows selection,
    with support for custom item activation callbacks.

    Signals:
        video_selected (ReleaseVideo): Emitted when a video is selected
    """

    # Signal emitted when a video is selected
    video_selected = QtCore.pyqtSignal(ReleaseVideo)

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        """
        Initialize the playlist widget.

        Args:
            parent (Optional[QWidget]): Parent widget
        """
        super().__init__(parent)

        # Configure appearance
        self.setStyleSheet("""
            QListWidget {
                background-color: black;
                color: white;
                border: 1px solid #333;
                selection-background-color: #444;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #333;
            }
            QListWidget::item:selected {
                background-color: #555;
            }
        """)

        # Set size policy
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumWidth(200)

        # Connect signals
        self.itemActivated.connect(self._on_item_activated)

    def set_videos(self, videos: List[ReleaseVideo]) -> None:
        """
        Set the list of videos to display.

        Args:
            videos (List[ReleaseVideo]): List of video items to display
        """
        self.clear()

        for video in videos:
            item = QtWidgets.QListWidgetItem(video.display_name)
            item.setData(QtCore.Qt.UserRole, video)
            self.addItem(item)

        logger.info(f"Loaded {len(videos)} videos into playlist")

    def add_video(self, video: ReleaseVideo) -> None:
        """
        Add a single video to the playlist.

        Args:
            video (ReleaseVideo): Video to add
        """
        item = QtWidgets.QListWidgetItem(video.display_name)
        item.setData(QtCore.Qt.UserRole, video)
        self.addItem(item)

    def get_selected_video(self) -> Optional[ReleaseVideo]:
        """
        Get the currently selected video.

        Returns:
            Optional[ReleaseVideo]: The selected video, or None if none selected
        """
        current_item = self.currentItem()
        if current_item:
            return current_item.data(QtCore.Qt.UserRole)
        return None

    def select_video(self, video: ReleaseVideo) -> None:
        """
        Select a specific video in the playlist.

        Args:
            video (ReleaseVideo): Video to select
        """
        for i in range(self.count()):
            item = self.item(i)
            item_video = item.data(QtCore.Qt.UserRole)
            if item_video and item_video.asset_url == video.asset_url:
                self.setCurrentItem(item)
                break

    def clear_playlist(self) -> None:
        """Clear all items from the playlist."""
        self.clear()

    def _on_item_activated(self, item: QtWidgets.QListWidgetItem) -> None:
        """
        Handle item activation (double-click or Enter).

        Args:
            item (QListWidgetItem): The activated item
        """
        video = item.data(QtCore.Qt.UserRole)
        if video:
            logger.info(f"Video selected: {video.display_name}")
            self.video_selected.emit(video)
        else:
            logger.warning("Activated item has no video data")

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Handle key press events for custom navigation.

        Args:
            event (QKeyEvent): The key event
        """
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            current_item = self.currentItem()
            if current_item:
                self._on_item_activated(current_item)
            event.accept()
        else:
            super().keyPressEvent(event)
