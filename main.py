#!/usr/bin/env python3
"""Video Terminal - Main entry point

Simple PyQt5 application for Linux that displays a video player (using vlc),
release text from GitHub, a playlist of releases with .webm assets, and an
embedded xterm terminal in the lower-right pane.
"""

import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from controllers.app_controller import ApplicationController


def main():
    """Main application entry point."""
    try:
        controller = ApplicationController()
        exit_code = controller.run()
        controller.cleanup()
        return exit_code
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
        return 1
    except Exception as e:
        print(f"Application error: {e}")
        logging.error("Unhandled application error", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())