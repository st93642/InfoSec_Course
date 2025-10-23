# Video Terminal - Pilot (Linux) — Python PyQt5 version

Simple pilot application that displays a video player, text content from GitHub releases, a playlist, and an embedded terminal.

Features

- Upper-left: video player (plays .webm downloaded from GitHub release assets using VLC)
- Upper-right: textual content (release body)
- Lower-left: playlist of available releases with .webm assets
- Lower-right: embedded terminal (uses xterm -into)
- Playback controls: play/pause buttons, seek slider, volume slider
- Download progress: progress bar shows download status

Requirements (Linux)

- Python 3.8+
- PyQt5
- python-vlc (requires VLC installed)
- requests
- System: X11-based desktop (xterm embedding uses X11 window IDs)
- VLC installed (for python-vlc to work)
- xterm installed (or modify code to use another terminal emulator)

Install Python dependencies

On newer Debian/Ubuntu systems, pip installs are restricted. Use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or, if you prefer system-wide (not recommended), use:

```bash
python3 -m pip install --break-system-packages -r requirements.txt
```

Install system packages (Debian/Ubuntu example)

```bash
sudo apt update
sudo apt install -y vlc xterm
```

Running the app

1. Optionally export the repo you want to point to:

```bash
export GITHUB_REPO="st93642/Assets"
```

2. If using virtual environment, activate it:

```bash
source venv/bin/activate
```

3. Run:

```bash
python main.py
```

Or use the launcher script:

```bash
./run.sh
```

Notes

- Downloads are cached in `./video_terminal_cache/<owner_repo>/` (inside the directory where you run the app) so they are visible to the user.
- The app uses VLC for video playback via python-vlc. Ensure VLC is installed and accessible.
- Embedding terminals requires xterm. If you don't have xterm, the app will attempt to open an external terminal.
- If python-vlc cannot find VLC, ensure VLC is installed and available on the PATH.

Limitations and next steps

- Add better error handling and progress UI when downloading large assets.
- Support authentication for private repositories.
- Add play/pause/seek controls and video metadata UI.
