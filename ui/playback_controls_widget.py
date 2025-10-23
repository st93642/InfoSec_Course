"""Playback controls widget for video playback control."""

import logging
from typing import Callable, Optional

from PyQt5 import QtCore, QtWidgets

logger = logging.getLogger(__name__)


class PlaybackControlsWidget(QtWidgets.QWidget):
    """
    Widget providing playback controls for video content.

    This widget includes play/pause buttons, seek slider, volume slider,
    and progress display.

    Signals:
        play_requested (): Emitted when play is requested
        pause_requested (): Emitted when pause is requested
        seek_requested (float): Emitted when seek position changes (0.0-1.0)
        volume_changed (int): Emitted when volume changes (0-100)
    """

    # Signals
    play_requested = QtCore.pyqtSignal()
    pause_requested = QtCore.pyqtSignal()
    seek_requested = QtCore.pyqtSignal(float)
    volume_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        """
        Initialize the playback controls widget.

        Args:
            parent (Optional[QWidget]): Parent widget
        """
        super().__init__(parent)

        self._is_playing = False
        self._current_position = 0.0
        self._volume = 50

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self) -> None:
        """Set up the user interface."""
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # Play/Pause button
        # Show combined label 'Play/Pause' as the default, but toggle to
        # 'Pause' when playing and 'Play/Pause' when stopped for clarity.
        self.play_button = QtWidgets.QPushButton("Play/Pause")
        self.play_button.setFixedWidth(80)

        # Seek slider
        self.seek_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.seek_slider.setRange(0, 100)
        self.seek_slider.setValue(0)
        self.seek_slider.setEnabled(False)  # Disabled until video is loaded

        # Volume controls
        volume_label = QtWidgets.QLabel("Vol:")
        volume_label.setStyleSheet("color: white;")
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self._volume)
        self.volume_slider.setFixedWidth(80)

        # Progress bar for downloads
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedWidth(150)

        # Add widgets to layout
        layout.addWidget(self.play_button)
        layout.addWidget(QtWidgets.QLabel("Seek:"))  # Seek label
        layout.addWidget(self.seek_slider, 1)  # Stretch factor 1
        layout.addWidget(volume_label)
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.progress_bar)

        # Set overall styling
        self.setStyleSheet("""
            QWidget {
                background-color: #222;
                color: white;
            }
            QPushButton {
                background-color: #444;
                color: white;
                border: 1px solid #666;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QSlider::groove:horizontal {
                border: 1px solid #999;
                height: 8px;
                background: #333;
                margin: 2px 0;
            }
            QSlider::handle:horizontal {
                background: #666;
                border: 1px solid #999;
                width: 18px;
                margin: -2px 0;
                border-radius: 3px;
            }
            QProgressBar {
                border: 1px solid #666;
                border-radius: 3px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
            }
        """)

    def _connect_signals(self) -> None:
        """Connect widget signals to handlers."""
        self.play_button.clicked.connect(self._on_play_clicked)
        self.seek_slider.sliderMoved.connect(self._on_seek_changed)
        self.volume_slider.sliderMoved.connect(self._on_volume_changed)

    def _on_play_clicked(self) -> None:
        """Handle play/pause button clicks."""
        if self._is_playing:
            self.pause_requested.emit()
            self._set_playing_state(False)
        else:
            self.play_requested.emit()
            self._set_playing_state(True)

    def _on_seek_changed(self, position: int) -> None:
        """Handle seek slider changes."""
        if self.seek_slider.isEnabled():
            position_fraction = position / 100.0
            self.seek_requested.emit(position_fraction)
            logger.debug(f"Seek requested: {position_fraction}")

    def _on_volume_changed(self, volume: int) -> None:
        """Handle volume slider changes."""
        self._volume = volume
        self.volume_changed.emit(volume)
        logger.debug(f"Volume changed: {volume}")

    def _set_playing_state(self, is_playing: bool) -> None:
        """Update the play/pause button state."""
        self._is_playing = is_playing
        # When playing, show 'Pause' to indicate available action.
        # When not playing, show the combined label 'Play/Pause'.
        self.play_button.setText("Pause" if is_playing else "Play/Pause")

    def set_playing(self, is_playing: bool) -> None:
        """
        Update the playing state.

        Args:
            is_playing (bool): Whether video is currently playing
        """
        self._set_playing_state(is_playing)

    def set_position(self, position: float) -> None:
        """
        Update the seek position.

        Args:
            position (float): Position as fraction (0.0-1.0)
        """
        if self.seek_slider.isEnabled():
            self._current_position = position
            slider_value = int(position * 100)
            self.seek_slider.setValue(slider_value)

    def enable_controls(self, enabled: bool = True) -> None:
        """
        Enable or disable playback controls.

        Args:
            enabled (bool): Whether controls should be enabled
        """
        self.seek_slider.setEnabled(enabled)
        self.play_button.setEnabled(enabled)

    def show_download_progress(self, show: bool = True) -> None:
        """
        Show or hide the download progress bar.

        Args:
            show (bool): Whether to show the progress bar
        """
        self.progress_bar.setVisible(show)
        if not show:
            self.progress_bar.setValue(0)

    def set_download_progress(self, downloaded: int, total: int) -> None:
        """
        Update download progress.

        Args:
            downloaded (int): Bytes downloaded
            total (int): Total bytes to download
        """
        if total > 0:
            percentage = int((downloaded / total) * 100)
            self.progress_bar.setValue(percentage)
        else:
            self.progress_bar.setValue(0)

    def reset_position(self) -> None:
        """Reset the seek position to the beginning."""
        self.set_position(0.0)

    def get_volume(self) -> int:
        """
        Get the current volume level.

        Returns:
            int: Volume level (0-100)
        """
        return self._volume

    def set_volume(self, volume: int) -> None:
        """
        Set the volume level.

        Args:
            volume (int): Volume level (0-100)
        """
        self._volume = max(0, min(100, volume))
        self.volume_slider.setValue(self._volume)
