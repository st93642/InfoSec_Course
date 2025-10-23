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

        # Create main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Add search/filter box
        self.search_box = QtWidgets.QLineEdit()
        self.search_box.setPlaceholderText("Search videos...")
        self.search_box.textChanged.connect(self._filter_videos)
        self.search_box.setStyleSheet("""
            QLineEdit {
                background-color: #333;
                color: white;
                border: 1px solid #666;
                padding: 5px;
                border-radius: 3px;
            }
        """)
        main_layout.addWidget(self.search_box)

        # Create tree widget
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.setColumnCount(1)
        self.tree_widget.setRootIsDecorated(True)
        self.tree_widget.setItemsExpandable(True)

        # Set up icons for different item types
        self.folder_icon = self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon)
        self.file_icon = self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)

        # Configure tree widget appearance
        self.tree_widget.setStyleSheet("""
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
        self.tree_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tree_widget.setMinimumWidth(200)

        main_layout.addWidget(self.tree_widget)

        # Connect tree widget signals
        self.tree_widget.itemActivated.connect(self._on_item_activated)
        self.tree_widget.itemClicked.connect(self._on_item_clicked)

        # Store all items for filtering
        self.all_items = []

    def set_videos(self, videos: List[ReleaseVideo]) -> None:
        """
        Set the list of videos to display.

        Args:
            videos (List[ReleaseVideo]): List of video items to display
        """
        self.tree_widget.clear()
        self.all_items = []

        for video in videos:
            item = QtWidgets.QTreeWidgetItem([video.display_name])
            item.setData(0, QtCore.Qt.UserRole, video)
            self.tree_widget.addTopLevelItem(item)
            self.all_items.append(item)

        logger.info(f"Loaded {len(videos)} videos into playlist")

    def add_video(self, video: ReleaseVideo) -> None:
        """
        Add a single video to the playlist as a top-level item.

        Args:
            video (ReleaseVideo): Video to add
        """
        # Create display name without release tag
        display_name = video.display_name
        item = QtWidgets.QTreeWidgetItem([display_name])
        item.setData(0, QtCore.Qt.UserRole, video)
        # Set file icon for video items
        item.setIcon(0, self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))
        self.tree_widget.addTopLevelItem(item)
        self.all_items.append(item)

    def add_category(self, category_name: str) -> QtWidgets.QTreeWidgetItem:
        """
        Add a category (top-level item) to the playlist.

        Args:
            category_name (str): Name of the category

        Returns:
            QtWidgets.QTreeWidgetItem: The created category item
        """
        category_item = QtWidgets.QTreeWidgetItem([category_name])
        # Set folder icon for category items
        category_item.setIcon(0, self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon))
        self.tree_widget.addTopLevelItem(category_item)
        self.all_items.append(category_item)
        return category_item

    def add_subcategory(self, parent_item: QtWidgets.QTreeWidgetItem, subcategory_name: str) -> QtWidgets.QTreeWidgetItem:
        """
        Add a subcategory under a parent item.

        Args:
            parent_item (QtWidgets.QTreeWidgetItem): Parent item to add subcategory under
            subcategory_name (str): Name of the subcategory

        Returns:
            QtWidgets.QTreeWidgetItem: The created subcategory item
        """
        subcategory_item = QtWidgets.QTreeWidgetItem([subcategory_name])
        # Set folder icon for subcategory items
        subcategory_item.setIcon(0, self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon))
        parent_item.addChild(subcategory_item)
        self.all_items.append(subcategory_item)
        return subcategory_item

    def add_video_to_category(self, parent_item: QtWidgets.QTreeWidgetItem, video: ReleaseVideo) -> None:
        """
        Add a video under a category or subcategory.

        Args:
            parent_item (QtWidgets.QTreeWidgetItem): Parent item to add video under
            video (ReleaseVideo): Video to add
        """
        # Create display name without release tag
        display_name = video.display_name
        video_item = QtWidgets.QTreeWidgetItem([display_name])
        video_item.setData(0, QtCore.Qt.UserRole, video)
        # Set file icon for video items
        video_item.setIcon(0, self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))
        parent_item.addChild(video_item)
        self.all_items.append(video_item)

    def get_next_video(self, current_video: Optional[ReleaseVideo]) -> Optional[ReleaseVideo]:
        """Return the next video item after the given video in tree order."""
        if current_video is None:
            return None

        iterator = QtWidgets.QTreeWidgetItemIterator(self.tree_widget)
        found_current = False

        while iterator.value():
            item = iterator.value()
            video = item.data(0, QtCore.Qt.UserRole)

            if video:
                if found_current and video.asset_url != current_video.asset_url:
                    return video

                if video.asset_url == current_video.asset_url:
                    found_current = True

            iterator += 1

        return None

    def get_selected_video(self) -> Optional[ReleaseVideo]:
        """
        Get the currently selected video.

        Returns:
            Optional[ReleaseVideo]: The selected video, or None if none selected
        """
        current_item = self.tree_widget.currentItem()
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
        for i in range(self.tree_widget.topLevelItemCount()):
            item = self.tree_widget.topLevelItem(i)
            result = find_video_item(item)
            if result:
                self.tree_widget.setCurrentItem(result)
                break

    def clear_playlist(self) -> None:
        """Clear all items from the playlist."""
        self.tree_widget.clear()

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
                self.tree_widget.collapseItem(item)
            else:
                self.tree_widget.expandItem(item)

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
            current_item = self.tree_widget.currentItem()
            if current_item:
                self._on_item_activated(current_item, 0)
            event.accept()
        else:
            super().keyPressEvent(event)

    def _filter_videos(self, text: str) -> None:
        """
        Filter videos based on search text. Shows items that contain the search text
        in their display name (case-insensitive).

        Args:
            text (str): Search text to filter by
        """
        search_text = text.lower().strip()

        def filter_item(item: QtWidgets.QTreeWidgetItem) -> bool:
            """Recursively filter an item and its children. Returns True if item should be visible."""
            item_text = item.text(0).lower()
            has_match = search_text in item_text

            # Check children
            child_visible = False
            for i in range(item.childCount()):
                child = item.child(i)
                if filter_item(child):
                    child_visible = True

            # Item is visible if it matches or has visible children
            visible = has_match or child_visible
            item.setHidden(not visible)
            return visible

        # Apply filter to all top-level items
        for i in range(self.tree_widget.topLevelItemCount()):
            filter_item(self.tree_widget.topLevelItem(i))

        # Expand all visible items to show matches
        def expand_visible_items(item: QtWidgets.QTreeWidgetItem) -> None:
            if not item.isHidden():
                item.setExpanded(True)
                for i in range(item.childCount()):
                    expand_visible_items(item.child(i))

        for i in range(self.tree_widget.topLevelItemCount()):
            expand_visible_items(self.tree_widget.topLevelItem(i))
