"""Configuration models for the Video Terminal application."""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ApplicationConfig:
    """
    Configuration settings for the Video Terminal application.

    This class centralizes all configuration options including environment variables,
    file paths, and application settings.

    Attributes:
        github_repo (str): The GitHub repository to fetch releases from (format: owner/repo)
        github_token (Optional[str]): GitHub personal access token for private repositories
        cache_directory (Path): Directory where downloaded videos are cached
        video_extensions (tuple): Supported video file extensions
        text_extensions (tuple): Supported text file extensions for descriptions
        network_timeout (int): Timeout in seconds for network requests
        download_chunk_size (int): Size of download chunks in bytes
        terminal_font_size (int): Font size for the embedded terminal
    """
    github_repo: str = "st93642/Assets"
    github_token: Optional[str] = None
    cache_directory: Path = Path.home() / "Downloads"
    video_extensions: tuple = (".webm", ".mp4", ".avi", ".mkv")
    text_extensions: tuple = (".txt", ".md")
    network_timeout: int = 30
    download_chunk_size: int = 8192
    terminal_font_size: int = 14

    @classmethod
    def from_environment(cls) -> 'ApplicationConfig':
        """
        Create configuration from environment variables.

        Returns:
            ApplicationConfig: Configuration instance with values from environment
        """
        return cls(
            github_repo=os.environ.get('GITHUB_REPO', cls.github_repo),
            github_token=os.environ.get('GITHUB_TOKEN'),
            cache_directory=Path(os.environ.get('CACHE_DIR', str(cls.cache_directory))),
            terminal_font_size=int(os.environ.get('TERMINAL_FONT_SIZE', cls.terminal_font_size))
        )

    def ensure_cache_directory_exists(self) -> None:
        """Ensure the cache directory exists, creating it if necessary."""
        self.cache_directory.mkdir(parents=True, exist_ok=True)

    def get_cache_path_for_asset(self, asset_name: str) -> Path:
        """
        Get the cache file path for a given asset name.

        Args:
            asset_name (str): The name of the asset file

        Returns:
            Path: The full path where the asset should be cached
        """
        return self.cache_directory / asset_name
