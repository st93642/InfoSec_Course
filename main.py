#!/usr/bin/env python3
"""Video Terminal - pilot

Simple PyQt5 application for Linux that displays a video player (using vlc),
release text from GitHub, a playlist of releases with .webm assets, and an
embedded xterm terminal in the lower-right pane.
"""

import os
import sys
import tempfile
import threading
import subprocess
import html
from pathlib import Path

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import vlc

# --- Configuration
GITHUB_REPO = os.environ.get('GITHUB_REPO', 'st93642/Assets')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}


class ReleaseVideo:
    def __init__(self, tag, body, asset_name, asset_url, description=""):
        self.tag = tag
        self.body = body
        self.asset_name = asset_name
        self.asset_url = asset_url
        self.description = description


def fetch_releases_with_webm(repo, tag=None):
    """Fetch releases from GitHub public API and filter assets ending with .webm."""
    url = f"https://api.github.com/repos/{repo}/releases"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    releases_data = resp.json()
    if tag:
        releases_data = [r for r in releases_data if r.get("tag_name") == tag]
    releases = []
    for r in releases_data:
        body = r.get("body", "")
        tag_name = r.get("tag_name") or r.get("name") or ""
        assets = {a.get("name"): a.get("browser_download_url") for a in r.get("assets", [])}
        for name, asset_url in assets.items():
            if name.lower().endswith((".webm", ".mp4")):
                description = ""
                txt_name = name.rsplit('.', 1)[0] + '.txt'
                if txt_name in assets:
                    try:
                        desc_resp = requests.get(assets[txt_name], headers=HEADERS, timeout=10)
                        desc_resp.raise_for_status()
                        description = desc_resp.text
                    except Exception:
                        pass  # fallback to empty
                releases.append(ReleaseVideo(tag_name, body, name, asset_url, description))
    return releases


def download_asset(url, dest: Path, progress_callback=None):
    if dest.exists():
        return dest
    with requests.get(url, headers=HEADERS, stream=True, timeout=30) as r:
        r.raise_for_status()
        total = int(r.headers.get('content-length', 0))
        downloaded = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1024 * 16):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if progress_callback and total > 0:
                        progress_callback(downloaded, total)
    return dest


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, selected_tag=None):
        super().__init__()
        self.selected_tag = selected_tag
        self.setWindowTitle("Video Terminal - Pilot")
        self.resize(1200, 800)
        self.setStyleSheet("QMainWindow { background-color: black; }")

        # Use a visible cache directory in the current working directory so users can see downloads easily
        self.cache_dir = Path(os.path.expanduser("~")) / "Downloads"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Main vertical layout: upper and lower
        central = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(central)

        upper = QtWidgets.QWidget()
        u_layout = QtWidgets.QHBoxLayout(upper)

        # Upper-left: video widget
        self.video_frame = QtWidgets.QFrame()
        self.video_frame.setStyleSheet("background: black")
        u_layout.addWidget(self.video_frame, 2)

        # Upper-right: text
        self.text = QtWidgets.QTextEdit()
        self.text.setReadOnly(True)
        self.text.setAcceptRichText(True)  # Allow HTML rendering
        self.text.setStyleSheet("background-color: black; color: lime;")
        u_layout.addWidget(self.text, 1)

        vlay.addWidget(upper, 3)

        # Playback controls under video
        controls_hbox = QtWidgets.QHBoxLayout()
        self.play_btn = QtWidgets.QPushButton('Play')
        self.pause_btn = QtWidgets.QPushButton('Pause')
        self.seek_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.download_progress = QtWidgets.QProgressBar()
        self.download_progress.setVisible(False)

        controls_hbox.addWidget(self.play_btn)
        controls_hbox.addWidget(self.pause_btn)
        controls_hbox.addWidget(QtWidgets.QLabel('Seek:'))
        controls_hbox.addWidget(self.seek_slider)
        controls_hbox.addWidget(QtWidgets.QLabel('Vol:'))
        controls_hbox.addWidget(self.volume_slider)
        controls_hbox.addWidget(self.download_progress)

        vlay.addLayout(controls_hbox)

        # Lower split: playlist (left) and terminal (right)
        lower = QtWidgets.QWidget()
        l_layout = QtWidgets.QHBoxLayout(lower)

        # Playlist
        self.playlist = QtWidgets.QListWidget()
        self.playlist.itemActivated.connect(self.on_playlist_activate)
        self.playlist.setStyleSheet("background-color: black; color: white;")
        l_layout.addWidget(self.playlist, 1)

        # Terminal placeholder
        self.terminal_container = QtWidgets.QWidget()
        self.terminal_container.setLayout(QtWidgets.QVBoxLayout())
        l_layout.addWidget(self.terminal_container, 1)  # Equal width

        vlay.addWidget(lower, 2)  # Make lower part taller

        # Status label at bottom
        self.status_label = QtWidgets.QLabel("Fetching video list...")
        self.status_label.setStyleSheet("color: white;")
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate
        self.progress_bar.setVisible(True)
        status_layout = QtWidgets.QHBoxLayout()
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.progress_bar)
        vlay.addLayout(status_layout)

        self.setCentralWidget(central)

        # VLC setup
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Connect controls
        self.play_btn.clicked.connect(self.player.play)
        self.pause_btn.clicked.connect(self.player.pause)
        self.seek_slider.sliderMoved.connect(self.on_seek)
        self.volume_slider.sliderMoved.connect(self.on_volume)

        # Timer to update seek slider
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_slider)
        self.update_timer.start(1000)  # Update every 1 second

        # spawn xterm in container
        # QtCore.QTimer.singleShot(500, self.spawn_xterm)  # Moved to main after show
        
        # Handle resize to update xterm geometry
        self.terminal_container.resizeEvent = self.on_terminal_resize

    def setup_vlc(self):
        if sys.platform.startswith("linux"):
            # For X11 embedding
            win_id = int(self.video_frame.winId())
            self.player.set_xwindow(win_id)

    def spawn_xterm(self):
        # Get the size of the terminal container
        size = self.terminal_container.size()
        cols = max(120, size.width() // 8)  # Larger default
        rows = max(40, size.height() // 16)
        geometry = f"{cols}x{rows}"
        
        # On Linux/X11 we can embed xterm by passing -into <winid>
        winid = int(self.terminal_container.winId())
        try:
            subprocess.Popen(["xterm", "-into", str(winid), "-geometry", geometry])
        except Exception as e:
            # fallback: open xterm normally
            subprocess.Popen(["xterm"]) 

    def load_releases(self):
        try:
            QtCore.QMetaObject.invokeMethod(self, "set_progress_visible", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(bool, True))
            items = fetch_releases_with_webm(GITHUB_REPO, self.selected_tag)
        except Exception as e:
            items = []
            QtCore.QMetaObject.invokeMethod(self, "set_text_sync", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"Error fetching releases: {e}"))
            QtCore.QMetaObject.invokeMethod(self, "set_status", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, "Error fetching releases"))

        QtCore.QMetaObject.invokeMethod(self, "set_progress_visible", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(bool, False))

        for rv in items:
            QtCore.QMetaObject.invokeMethod(self, "add_playlist_item", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(object, rv))

        if items:
            QtCore.QMetaObject.invokeMethod(self, "set_status", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, ""))
        else:
            QtCore.QMetaObject.invokeMethod(self, "set_status", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, "No videos found"))

    @QtCore.pyqtSlot(object)
    def add_playlist_item(self, rv):
        item = QtWidgets.QListWidgetItem(f"{rv.tag} — {rv.asset_name}")
        item.setData(QtCore.Qt.UserRole, rv)
        self.playlist.addItem(item)

    @QtCore.pyqtSlot(str)
    def set_text_sync(self, txt):
        self.text.setPlainText(txt)

    @QtCore.pyqtSlot(str)
    def set_status(self, msg):
        self.status_label.setText(msg)

    @QtCore.pyqtSlot(bool)
    def set_progress_visible(self, visible):
        self.progress_bar.setVisible(visible)

    def on_seek(self, position):
        if self.player.get_length() > 0:
            self.player.set_position(position / 100.0)

    def on_volume(self, volume):
        self.player.audio_set_volume(volume)

    def update_slider(self):
        if self.player.get_length() > 0:
            position = self.player.get_position() * 100
            self.seek_slider.setValue(int(position))

    def on_terminal_resize(self, event):
        # Update xterm geometry on resize
        size = self.terminal_container.size()
        cols = max(80, size.width() // 8)
        rows = max(24, size.height() // 16)
        # Note: xterm doesn't support dynamic resize via -geometry after launch
        # This is a placeholder; full dynamic resize might require killing and restarting xterm
        pass

    def on_playlist_activate(self, item):
        rv: ReleaseVideo = item.data(QtCore.Qt.UserRole)
        text_content = html.unescape(rv.description) if rv.description else rv.body
        self.text.setHtml(text_content)

        # download and play
        dest = self.cache_dir / rv.asset_name
        threading.Thread(target=self._download_and_play, args=(rv.asset_url, dest), daemon=True).start()

    def _download_and_play(self, url, dest):
        try:
            self.download_progress.setVisible(True)
            self.download_progress.setRange(0, 100)
            def update_progress(downloaded, total):
                percent = int((downloaded / total) * 100)
                self.download_progress.setValue(percent)
            download_asset(url, dest, update_progress)
            self.download_progress.setVisible(False)
            # Invoke play in main thread
            QtCore.QMetaObject.invokeMethod(self, "play_video", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, str(dest)))
        except Exception as e:
            self.download_progress.setVisible(False)
            QtCore.QMetaObject.invokeMethod(self, "set_text_sync", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"Error downloading/playing: {e} for {dest}"))

    @QtCore.pyqtSlot(str)
    def play_video(self, dest):
        media = self.instance.media_new(dest)
        self.player.set_media(media)
        self.seek_slider.setValue(0)  # Reset slider to start
        self.player.play()


def main():
    app = QtWidgets.QApplication(sys.argv)

    # Choice dialog
    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle("Choose Section")
    dialog.setStyleSheet("QDialog { background-color: black; color: white; }")
    layout = QtWidgets.QVBoxLayout(dialog)
    label = QtWidgets.QLabel("Select the section of videos to fetch:")
    label.setStyleSheet("color: white;")
    layout.addWidget(label)
    intro_btn = QtWidgets.QPushButton("Intro to Linux")
    intro_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    sysadmin_btn = QtWidgets.QPushButton("System Administration")
    sysadmin_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    netadmin_btn = QtWidgets.QPushButton("Network administration")
    netadmin_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    winadmin_btn = QtWidgets.QPushButton("Windows administration")
    winadmin_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    db_btn = QtWidgets.QPushButton("Data Bases")
    db_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    python_btn = QtWidgets.QPushButton("Python")
    python_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    infosec_btn = QtWidgets.QPushButton("InfoSec")
    infosec_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    security_btn = QtWidgets.QPushButton("Security Analysis")
    security_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    infosec_systems_btn = QtWidgets.QPushButton("InfoSec Systems")
    infosec_systems_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    incident_response_btn = QtWidgets.QPushButton("Incident Response")
    incident_response_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    compliance_btn = QtWidgets.QPushButton("Compliance assurance")
    compliance_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    app_security_btn = QtWidgets.QPushButton("App Security")
    app_security_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    bonus_btn = QtWidgets.QPushButton("Bonus Part")
    bonus_btn.setStyleSheet("QPushButton { background-color: #333; color: white; }")
    layout.addWidget(intro_btn)
    layout.addWidget(sysadmin_btn)
    layout.addWidget(netadmin_btn)
    layout.addWidget(winadmin_btn)
    layout.addWidget(db_btn)
    layout.addWidget(python_btn)
    layout.addWidget(infosec_btn)
    layout.addWidget(security_btn)
    layout.addWidget(infosec_systems_btn)
    layout.addWidget(incident_response_btn)
    layout.addWidget(compliance_btn)
    layout.addWidget(app_security_btn)
    layout.addWidget(bonus_btn)

    selected_tag = None

    def on_intro():
        nonlocal selected_tag
        selected_tag = "1.0.0"
        dialog.accept()

    def on_sysadmin():
        nonlocal selected_tag
        selected_tag = "2.0.0"
        dialog.accept()

    def on_netadmin():
        nonlocal selected_tag
        selected_tag = "3.0.0"
        dialog.accept()

    def on_winadmin():
        nonlocal selected_tag
        selected_tag = "4.0.0"
        dialog.accept()

    def on_db():
        nonlocal selected_tag
        selected_tag = "5.0.0"
        dialog.accept()

    def on_python():
        nonlocal selected_tag
        selected_tag = "6.0.0"
        dialog.accept()

    def on_infosec():
        nonlocal selected_tag
        selected_tag = "7.0.0"
        dialog.accept()

    def on_security():
        nonlocal selected_tag
        selected_tag = "8.0.0"
        dialog.accept()

    def on_infosec_systems():
        nonlocal selected_tag
        selected_tag = "9.0.0"
        dialog.accept()

    def on_incident_response():
        nonlocal selected_tag
        selected_tag = "10.0.0"
        dialog.accept()

    def on_compliance():
        nonlocal selected_tag
        selected_tag = "11.0.0"
        dialog.accept()

    def on_app_security():
        nonlocal selected_tag
        selected_tag = "12.0.0"
        dialog.accept()

    def on_bonus():
        nonlocal selected_tag
        selected_tag = "13.0.0"
        dialog.accept()

    intro_btn.clicked.connect(on_intro)
    sysadmin_btn.clicked.connect(on_sysadmin)
    netadmin_btn.clicked.connect(on_netadmin)
    winadmin_btn.clicked.connect(on_winadmin)
    db_btn.clicked.connect(on_db)
    python_btn.clicked.connect(on_python)
    infosec_btn.clicked.connect(on_infosec)
    security_btn.clicked.connect(on_security)
    infosec_systems_btn.clicked.connect(on_infosec_systems)
    incident_response_btn.clicked.connect(on_incident_response)
    compliance_btn.clicked.connect(on_compliance)
    app_security_btn.clicked.connect(on_app_security)
    bonus_btn.clicked.connect(on_bonus)

    dialog.exec_()

    if selected_tag is None:
        return  # No choice, exit

    w = MainWindow(selected_tag)
    w.show()
    w.setup_vlc()
    w.spawn_xterm()
    QtCore.QTimer.singleShot(0, lambda: threading.Thread(target=w.load_releases, daemon=True).start())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()