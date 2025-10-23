# Video Terminal - AI Coding Guidelines

## Project Architecture

**Single-file PyQt5 application** with embedded video player, GitHub integration, and terminal. Core structure:
- `MainWindow` class manages 4-pane UI: video (VLC) | text content | playlist | embedded xterm
- `ReleaseVideo` class represents GitHub release assets with .webm/.mp4 files
- Downloads cache to `~/Downloads/` for user visibility

## Key Patterns & Conventions

### UI Layout Management
- Uses `QHBoxLayout`/`QVBoxLayout` with stretch factors (e.g., `addWidget(widget, 2)`)
- Black theme: `background-color: black; color: lime/white`
- Responsive controls: seek/volume sliders update via 1-second timer

### GitHub Integration
- Fetches releases via public API: `https://api.github.com/repos/{repo}/releases`
- Filters assets by `.webm`/`.mp4` extensions
- Pairs video files with `.txt` descriptions from same release
- Supports `GITHUB_TOKEN` for private repos

### Video Playback
- VLC integration via `python-vlc` with X11 embedding: `player.set_xwindow(win_id)`
- Threaded downloads with progress callbacks updating `QProgressBar`
- Seek/volume controls connect to VLC player methods

### Terminal Embedding
- Xterm embedding: `subprocess.Popen(["xterm", "-into", str(win_id)])`
- Dynamic geometry calculation: `cols = width // 8`, `rows = height // 16`
- Fallback to external terminal if embedding fails

### Threading & UI Updates
- Network operations in background threads
- UI updates via `QtCore.QMetaObject.invokeMethod()` with `QtCore.Qt.QueuedConnection`
- Download progress updates main thread safely

## Development Workflow

### Setup Requirements
```bash
# System dependencies (Ubuntu/Debian)
sudo apt install vlc xterm

# Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the Application
```bash
# Set target repository
export GITHUB_REPO="st93642/Assets"

# Launch options
python main.py          # Direct execution
./run.sh               # Via launcher script
```

### Build Considerations
- **No build step** - pure Python with system dependencies
- Virtual environment required for dependency isolation
- VLC/python-vlc binding requires system VLC installation

## Code Style & Patterns

### Error Handling
- Network requests use `timeout=10/30` with `resp.raise_for_status()`
- Broad `except Exception` blocks with user-friendly error messages
- Graceful fallbacks (external terminal, cached content)

### Data Flow
- GitHub API → `fetch_releases_with_webm()` → `ReleaseVideo` objects
- Playlist selection → threaded download → VLC playback
- Text content: HTML-unescaped descriptions or release bodies

### Configuration
- Environment variables: `GITHUB_REPO`, `GITHUB_TOKEN`
- Default repo: `st93642/Assets`
- Cache directory: `~/Downloads/` (user-visible)

## Common Pitfalls

- **X11 embedding**: Requires display server, fails in headless environments
- **VLC dependencies**: System VLC must match python-vlc version
- **Threading**: All UI updates must be marshaled to main thread
- **File paths**: Use `Path` objects, expand user paths with `os.path.expanduser()`

## Testing Approach

- **Manual testing**: UI responsiveness, video playback, terminal embedding
- **Network testing**: Mock GitHub API responses for offline development
- **Cross-platform**: Linux-only due to X11/xterm dependencies

## Performance Considerations

- **Memory usage**: ~50-80MB baseline, spikes during video buffering
- **Network**: Downloads cached locally, API calls use requests with timeouts
- **UI**: Timer-based updates (1s interval) for seek position
- **Threading**: Background downloads prevent UI blocking</content>
<parameter name="filePath">/home/altin/Desktop/InfoSec_Course/.github/copilot-instructions.md