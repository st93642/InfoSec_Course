"""Application controller for managing the Video Terminal application."""

import logging
import sys
from typing import Dict, Optional

from PyQt5 import QtWidgets

from models.config import ApplicationConfig
from ui.main_window import MainWindow

logger = logging.getLogger(__name__)


class ApplicationController:
    """
    Main application controller.

    This controller manages the application lifecycle, configuration,
    and coordinates between different components.

    Attributes:
        config (ApplicationConfig): Application configuration
        app (QtWidgets.QApplication): Qt application instance
        main_window (Optional[MainWindow]): Main application window
    """

    # Course sections mapping
    COURSE_SECTIONS = {
        "Intro to Linux": "1.0.0",
        "System Administration": "2.0.0",
        "Network administration": "3.0.0",
        "Windows administration": "4.0.0",
        "Data Bases": "5.0.0",
        "Python": "6.0.0",
        "InfoSec": "7.0.0",
        "Security Analysis": "8.0.0",
        "InfoSec Systems": "9.0.0",
        "Incident Response": "10.0.0",
        "Compliance assurance": "11.0.0",
        "App Security": "12.0.0",
        "Bonus Part": "13.0.0"
    }

    def __init__(self):
        """Initialize the application controller."""
        self.config = ApplicationConfig.from_environment()
        self.app: Optional[QtWidgets.QApplication] = None
        self.main_window: Optional[MainWindow] = None

        # Ensure cache directory exists
        self.config.ensure_cache_directory_exists()

        logger.info("Application controller initialized")

    def run(self) -> int:
        """
        Run the application.

        Returns:
            int: Application exit code
        """
        try:
            # Create Qt application
            self.app = QtWidgets.QApplication(sys.argv)

            # Show section selection dialog
            selected_tag = self._show_section_selection_dialog()
            if selected_tag is None:
                logger.info("No section selected, exiting")
                return 0

            # Create and show main window
            self.main_window = MainWindow(self.config, selected_tag)
            self.main_window.show()

            # Load videos
            self.main_window.load_videos()

            # Start event loop
            logger.info("Starting Qt event loop")
            return self.app.exec_()

        except Exception as e:
            logger.error(f"Application error: {e}")
            return 1

    def _show_section_selection_dialog(self) -> Optional[str]:
        """
        Show the course section selection dialog.

        Returns:
            Optional[str]: Selected tag, or None if cancelled
        """
        dialog = SectionSelectionDialog(self.COURSE_SECTIONS)
        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            return dialog.get_selected_tag()

        return None

    def cleanup(self) -> None:
        """Clean up application resources."""
        logger.info("Cleaning up application controller")

        if self.main_window:
            self.main_window.close()

        if self.app:
            self.app.quit()


class SectionSelectionDialog(QtWidgets.QDialog):
    """
    Dialog for selecting a course section.

    This dialog presents the available course sections and allows
    the user to choose which section to load.
    """

    def __init__(self, sections: Dict[str, str], parent=None):
        """
        Initialize the section selection dialog.

        Args:
            sections (Dict[str, str]): Mapping of section names to tags
            parent: Parent widget
        """
        super().__init__(parent)

        self.sections = sections
        self.selected_tag: Optional[str] = None

        self.setWindowTitle("Choose Section")
        self.setStyleSheet("""
            QDialog {
                background-color: black;
                color: white;
            }
            QPushButton {
                background-color: #333;
                color: white;
                border: 1px solid #666;
                padding: 8px 16px;
                margin: 2px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QLabel {
                color: white;
                font-size: 14pt;
                margin-bottom: 10px;
            }
        """)

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Set up the dialog user interface."""
        layout = QtWidgets.QVBoxLayout(self)

        # Title label
        title_label = QtWidgets.QLabel("Select the section of videos to fetch:")
        title_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(title_label)

        # Create buttons for each section
        for section_name, tag in self.sections.items():
            button = QtWidgets.QPushButton(section_name)
            button.clicked.connect(lambda checked, t=tag: self._on_section_selected(t))
            layout.addWidget(button)

        # Set dialog properties
        self.setMinimumWidth(300)

    def _on_section_selected(self, tag: str) -> None:
        """
        Handle section selection.

        Args:
            tag (str): Selected section tag
        """
        self.selected_tag = tag
        self.accept()

    def get_selected_tag(self) -> Optional[str]:
        """
        Get the selected tag.

        Returns:
            Optional[str]: Selected tag, or None if none selected
        """
        return self.selected_tag
