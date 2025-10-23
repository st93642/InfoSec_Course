"""Download service for handling asset downloads with progress tracking."""

import logging
from pathlib import Path
from typing import Callable, Optional

import requests

from models.config import ApplicationConfig

logger = logging.getLogger(__name__)


class DownloadService:
    """
    Service for downloading assets with progress tracking and caching.

    This service handles HTTP downloads with progress callbacks, caching,
    and error handling.

    Attributes:
        config (ApplicationConfig): Application configuration
        session (requests.Session): HTTP session for downloads
    """

    def __init__(self, config: ApplicationConfig):
        """
        Initialize the download service.

        Args:
            config (ApplicationConfig): Application configuration
        """
        self.config = config
        self.session = requests.Session()

        # Set up headers for downloads
        self.session.headers.update({
            'User-Agent': 'VideoTerminal/1.0'
        })

    def download_asset(
        self,
        url: str,
        destination: Path,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> Path:
        """
        Download an asset to the specified destination with progress tracking.

        Args:
            url (str): URL of the asset to download
            destination (Path): Destination file path
            progress_callback (Optional[Callable[[int, int], None]]): Callback for progress updates
                Receives (downloaded_bytes, total_bytes) parameters

        Returns:
            Path: Path to the downloaded file

        Raises:
            requests.RequestException: If the download fails
            OSError: If writing to the destination fails
        """
        if destination.exists():
            logger.info(f"Asset already exists at {destination}")
            return destination

        logger.info(f"Downloading {url} to {destination}")

        try:
            with self.session.get(url, stream=True, timeout=self.config.network_timeout) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))

                downloaded = 0
                destination.parent.mkdir(parents=True, exist_ok=True)

                with open(destination, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=self.config.download_chunk_size):
                        if chunk:
                            file.write(chunk)
                            downloaded += len(chunk)

                            if progress_callback and total_size > 0:
                                progress_callback(downloaded, total_size)

                logger.info(f"Successfully downloaded {downloaded} bytes to {destination}")
                return destination

        except requests.RequestException as e:
            logger.error(f"Download failed for {url}: {e}")
            # Clean up partial download
            if destination.exists():
                destination.unlink()
            raise
        except OSError as e:
            logger.error(f"Failed to write to {destination}: {e}")
            raise

    def get_cached_asset_path(self, asset_name: str) -> Path:
        """
        Get the cached path for an asset.

        Args:
            asset_name (str): Name of the asset

        Returns:
            Path: Full path where the asset should be cached
        """
        return self.config.get_cache_path_for_asset(asset_name)

    def is_asset_cached(self, asset_name: str) -> bool:
        """
        Check if an asset is already cached.

        Args:
            asset_name (str): Name of the asset

        Returns:
            bool: True if the asset exists in cache
        """
        cache_path = self.get_cached_asset_path(asset_name)
        return cache_path.exists() and cache_path.is_file()

    def get_download_size(self, url: str) -> Optional[int]:
        """
        Get the size of a downloadable asset without downloading it.

        Args:
            url (str): URL of the asset

        Returns:
            Optional[int]: Size in bytes, or None if size cannot be determined
        """
        try:
            response = self.session.head(url, timeout=self.config.network_timeout)
            response.raise_for_status()
            content_length = response.headers.get('content-length')
            if content_length is not None:
                return int(content_length)
            return None
        except (requests.RequestException, ValueError):
            return None
