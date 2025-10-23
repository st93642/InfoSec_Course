"""Playlist widget for displaying and selecting video items."""

import logging
from typing import Callable, List, Optional

from PyQt5 import QtCore, QtGui, QtWidgets

from models.release_video import ReleaseVideo

logger = logging.getLogger(__name__)


class PlaylistWidget(QtWidgets.QTreeWidget):
    """
    Widget for displaying a playlist of video items in a tree structure.

    This widget shows available videos organized by categories,
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

        # Configure tree widget
        self.setHeaderHidden(True)
        self.setColumnCount(1)
        self.setRootIsDecorated(True)  # Show expansion indicators
        self.setItemsExpandable(True)  # Allow items to be expandable

        # Set up icons for different item types
        self.folder_icon = self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon)
        self.file_icon = self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)

        # Configure appearance
        self.setStyleSheet("""
            QTreeWidget {
                background-color: black;
                color: white;
                border: 1px solid #333;
                selection-background-color: #444;
            }
            QTreeWidget::item {
                padding: 5px;
                border-bottom: 1px solid #333;
            }
            QTreeWidget::item:selected {
                background-color: #555;
            }
            QTreeWidget::branch:has-children:!has-siblings:closed,
            QTreeWidget::branch:closed:has-children:has-siblings {
                border-image: none;
                image: none;
            }
            QTreeWidget::branch:open:has-children:!has-siblings,
            QTreeWidget::branch:open:has-children:has-siblings {
                border-image: none;
                image: none;
            }
        """)

        # Set size policy
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumWidth(200)

        # Connect signals
        self.itemActivated.connect(self._on_item_activated)
        self.itemClicked.connect(self._on_item_clicked)

    def set_videos(self, videos: List[ReleaseVideo]) -> None:
        """
        Set the list of videos to display.

        Args:
            videos (List[ReleaseVideo]): List of video items to display
        """
        self.clear()

        for video in videos:
            item = QtWidgets.QTreeWidgetItem([video.display_name])
            item.setData(0, QtCore.Qt.UserRole, video)
            self.addTopLevelItem(item)

        logger.info(f"Loaded {len(videos)} videos into playlist")

    def add_video(self, video: ReleaseVideo) -> None:
        """
        Add a single video to the playlist as a top-level item.

        Args:
            video (ReleaseVideo): Video to add
        """
        # Create display name with release information
        display_name = f"[{video.tag}] {video.display_name}"
        item = QtWidgets.QTreeWidgetItem([display_name])
        item.setData(0, QtCore.Qt.UserRole, video)
        self.addTopLevelItem(item)

    def add_category(self, category_name: str) -> QtWidgets.QTreeWidgetItem:
        """
        Add a category as a top-level item.

        Args:
            category_name (str): Name of the category

        Returns:
            QTreeWidgetItem: The category item for adding children
        """
        category_item = QtWidgets.QTreeWidgetItem([category_name])
        category_item.setData(0, QtCore.Qt.UserRole, None)  # No video data for categories
        category_item.setFlags(category_item.flags() | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        category_item.setIcon(0, self.folder_icon)  # Folder icon for categories
        self.addTopLevelItem(category_item)
        return category_item

    def add_subcategory(self, parent_item: QtWidgets.QTreeWidgetItem, subcategory_name: str) -> QtWidgets.QTreeWidgetItem:
        """
        Add a subcategory as a child of a parent item.

        Args:
            parent_item (QTreeWidgetItem): The parent item
            subcategory_name (str): Name of the subcategory

        Returns:
            QTreeWidgetItem: The subcategory item for adding children
        """
        subcategory_item = QtWidgets.QTreeWidgetItem([subcategory_name])
        subcategory_item.setData(0, QtCore.Qt.UserRole, None)  # No video data for categories
        subcategory_item.setFlags(subcategory_item.flags() | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        subcategory_item.setIcon(0, self.folder_icon)  # Folder icon for subcategories
        parent_item.addChild(subcategory_item)
        return subcategory_item

    def add_video_to_category(self, category_item: QtWidgets.QTreeWidgetItem, video: ReleaseVideo, display_name: Optional[str] = None) -> None:
        """
        Add a video as a child of a category item.

        Args:
            category_item (QTreeWidgetItem): The parent category item
            video (ReleaseVideo): Video to add
            display_name (Optional[str]): Custom display name, defaults to video.display_name
        """
        # Use custom display name if provided, otherwise use video's display name
        final_display_name = display_name if display_name is not None else video.display_name
        video_item = QtWidgets.QTreeWidgetItem([final_display_name])
        video_item.setData(0, QtCore.Qt.UserRole, video)
        video_item.setIcon(0, self.file_icon)  # File icon for videos
        category_item.addChild(video_item)

    def get_selected_video(self) -> Optional[ReleaseVideo]:
        """
        Get the currently selected video.

        Returns:
            Optional[ReleaseVideo]: The selected video, or None if none selected
        """
        current_item = self.currentItem()
        if current_item and current_item.data(0, QtCore.Qt.UserRole):
            return current_item.data(0, QtCore.Qt.UserRole)
        return None

    def select_video(self, video: ReleaseVideo) -> None:
        """
        Select a specific video in the playlist.

        Args:
            video (ReleaseVideo): Video to select
        """
        def find_video_item(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                child_video = child.data(0, QtCore.Qt.UserRole)
                if child_video and child_video.asset_url == video.asset_url:
                    return child
                # Recursively search in sub-items
                result = find_video_item(child)
                if result:
                    return result
            return None

        # Search all top-level items
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            result = find_video_item(item)
            if result:
                self.setCurrentItem(result)
                break

    def clear_playlist(self) -> None:
        """Clear all items from the playlist."""
        self.clear()

    def _on_item_clicked(self, item: QtWidgets.QTreeWidgetItem, column: int) -> None:
        """
        Handle item click (single click).

        Args:
            item (QTreeWidgetItem): The clicked item
            column (int): The column of the clicked item
        """
        video = item.data(0, QtCore.Qt.UserRole)
        if not video:
            # Category item clicked - expand/collapse
            if item.isExpanded():
                self.collapseItem(item)
            else:
                self.expandItem(item)

    def _on_item_activated(self, item: QtWidgets.QTreeWidgetItem, column: int) -> None:
        """
        Handle item activation (double-click or Enter).

        Args:
            item (QTreeWidgetItem): The activated item
            column (int): The column of the activated item
        """
        video = item.data(0, QtCore.Qt.UserRole)
        if video:
            logger.info(f"Video selected: {video.display_name}")
            self.video_selected.emit(video)
        # For category items, activation also expands/collapses (double-click behavior)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Handle key press events for custom navigation.

        Args:
            event (QKeyEvent): The key event
        """
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            current_item = self.currentItem()
            if current_item:
                self._on_item_activated(current_item, 0)
            event.accept()
        else:
            super().keyPressEvent(event)
