# Video Terminal - Pilot (Linux) — Python PyQt5 version

Simple pilot application that displays a video player, text content from GitHub releases, a playlist, and an embedded terminal.

## Project Structure

This application follows a modular, object-oriented architecture:

```text
├── controllers/          # Application controllers
│   └── app_controller.py # Main application controller
├── models/              # Data models and configuration
│   ├── config.py        # Application configuration
│   └── release_video.py # Video release data model
├── services/            # Business logic services
│   ├── download_service.py  # Asset downloading
│   ├── github_service.py    # GitHub API integration
│   ├── terminal_service.py  # Terminal embedding
│   └── video_service.py     # VLC video playback
├── ui/                  # User interface components
│   ├── main_window.py       # Main application window
│   ├── playlist_widget.py   # Video playlist display
│   ├── playback_controls_widget.py  # Video controls
│   ├── terminal_widget.py   # Terminal embedding widget
│   ├── text_content_widget.py       # Text display widget
│   └── video_widget.py      # Video display widget
├── tests/               # Comprehensive test suite
│   ├── conftest.py      # Test fixtures and configuration
│   ├── test_*.py        # Unit and integration tests
│   └── test_integration.py
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── run.sh              # Launcher script
└── pytest.ini          # Test configuration
```

## Features

- Upper-left: video player (plays .webm downloaded from GitHub release assets using VLC)
- Upper-right: textual content (release body or description from .txt files)
- Lower-left: playlist of available releases with .webm assets
- Lower-right: embedded terminal (uses xterm -into)
- Playback controls: play/pause buttons, seek slider, volume slider
- Download progress: progress bar shows download status
- Course section selection: Choose from InfoSec, Python, Linux, etc.

## Requirements (Linux)

- Python 3.8+
- PyQt5
- python-vlc (requires VLC installed)
- requests
- System: X11-based desktop (xterm embedding uses X11 window IDs)
- VLC installed (for python-vlc to work)
- xterm installed (or modify code to use another terminal emulator)

## Install Python dependencies

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

## Running the app

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

## Testing

The application includes a comprehensive test suite with unit tests, integration tests, and mocking for external dependencies.

### Running Tests

```bash
# Install test dependencies (included in requirements.txt)
pip install -r requirements.txt

# Run all tests
pytest

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only

# Run tests for specific module
pytest tests/test_models.py
```

### Test Structure

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test interactions between components
- **Mocking**: External dependencies (VLC, GitHub API, filesystem) are mocked
- **Coverage**: Target 80%+ code coverage across all modules

## Architecture Overview

### Core Components

1. **Application Controller** (`controllers/app_controller.py`)
   - Manages application lifecycle
   - Handles section selection dialog
   - Coordinates between services

2. **Data Models** (`models/`)
   - `ApplicationConfig`: Configuration management
   - `ReleaseVideo`: GitHub release video data

3. **Services** (`services/`)
   - `GitHubService`: GitHub API integration
   - `DownloadService`: Asset downloading with progress
   - `VideoService`: VLC video playback
   - `TerminalService`: xterm embedding

4. **UI Components** (`ui/`)
   - Modular widgets for each UI section
   - Signal-based communication
   - Qt event handling

### Key Design Patterns

- **Dependency Injection**: Services are injected into UI components
- **Observer Pattern**: Qt signals for component communication
- **Factory Pattern**: Service instantiation through configuration
- **Strategy Pattern**: Different download/cache strategies
- **Adapter Pattern**: VLC and xterm integration

## Development

### Code Quality

- Full type hints throughout codebase
- Comprehensive docstrings for all public APIs
- Modular architecture for maintainability
- Extensive test coverage

### Adding New Features

1. Create data models in `models/`
2. Implement business logic in `services/`
3. Build UI components in `ui/`
4. Add comprehensive tests
5. Update documentation

## Notes

- Downloads are cached in `~/Downloads/` so they are visible to the user.
- The app uses VLC for video playback via python-vlc. Ensure VLC is installed and accessible.
- Embedding terminals requires xterm. If you don't have xterm, the app will attempt to open an external terminal.
- If python-vlc cannot find VLC, ensure VLC is installed and available on the PATH.

## Limitations and next steps

- Add better error handling and progress UI when downloading large assets.
- Support authentication for private repositories.
- Add play/pause/seek controls and video metadata UI.
- Expand test coverage for UI components.
- Add configuration file support.
- Implement video format conversion.
- Add offline mode with cached content.
