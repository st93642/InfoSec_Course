"""GitHub service for fetching release information and assets."""

import logging
from typing import List, Optional
from urllib.parse import urlparse

import requests

from models.config import ApplicationConfig
from models.release_video import ReleaseVideo

logger = logging.getLogger(__name__)


class GitHubService:
    """
    Service for interacting with GitHub API to fetch releases and assets.

    This service handles authentication, API requests, and data transformation
    for GitHub release information.

    Attributes:
        config (ApplicationConfig): Application configuration
        session (requests.Session): HTTP session with authentication headers
    """

    def __init__(self, config: ApplicationConfig):
        """
        Initialize the GitHub service.

        Args:
            config (ApplicationConfig): Application configuration
        """
        self.config = config
        self.session = requests.Session()

        # Set up authentication headers
        headers = {'Accept': 'application/vnd.github.v3+json'}
        if config.github_token:
            headers['Authorization'] = f'token {config.github_token}'
        self.session.headers.update(headers)

    def fetch_releases(self, tag: Optional[str] = None) -> List[ReleaseVideo]:
        """
        Fetch releases from the configured GitHub repository.

        Args:
            tag (Optional[str]): Specific tag to fetch, or None for all releases

        Returns:
            List[ReleaseVideo]: List of video assets from releases

        Raises:
            requests.RequestException: If the API request fails
        """
        url = f"https://api.github.com/repos/{self.config.github_repo}/releases"

        try:
            logger.info(f"Fetching releases from {url}")
            response = self.session.get(url, timeout=self.config.network_timeout)
            response.raise_for_status()

            releases_data = response.json()
            if tag:
                releases_data = [r for r in releases_data if r.get("tag_name") == tag]

            return self._process_releases(releases_data)

        except requests.RequestException as e:
            logger.error(f"Failed to fetch releases: {e}")
            raise

    def _process_releases(self, releases_data: List[dict]) -> List[ReleaseVideo]:
        """
        Process raw release data into ReleaseVideo objects.

        Args:
            releases_data (List[dict]): Raw release data from GitHub API

        Returns:
            List[ReleaseVideo]: Processed video assets
        """
        videos = []

        for release in releases_data:
            release_videos = self._extract_videos_from_release(release)
            videos.extend(release_videos)

        logger.info(f"Found {len(videos)} video assets across {len(releases_data)} releases")
        return videos

    def _extract_videos_from_release(self, release: dict) -> List[ReleaseVideo]:
        """
        Extract video assets from a single release.

        Args:
            release (dict): Raw release data

        Returns:
            List[ReleaseVideo]: Video assets from this release
        """
        videos = []
        body = release.get("body", "")
        tag_name = release.get("tag_name") or release.get("name") or ""
        assets = {asset.get("name"): asset.get("browser_download_url")
                 for asset in release.get("assets", [])}

        for asset_name, asset_url in assets.items():
            if self._is_video_asset(asset_name):
                description = self._get_description_for_video(asset_name, assets)
                video = ReleaseVideo(
                    tag=tag_name,
                    body=body,
                    asset_name=asset_name,
                    asset_url=asset_url,
                    description=description
                )
                videos.append(video)

        return videos

    def _is_video_asset(self, asset_name: str) -> bool:
        """
        Check if an asset is a supported video file.

        Args:
            asset_name (str): Name of the asset

        Returns:
            bool: True if the asset is a supported video format
        """
        asset_lower = asset_name.lower()
        return any(asset_lower.endswith(ext) for ext in self.config.video_extensions)

    def _get_description_for_video(self, video_asset_name: str, assets: dict) -> Optional[str]:
        """
        Get the description text file that corresponds to a video asset.

        Args:
            video_asset_name (str): Name of the video asset
            assets (dict): Dictionary of all assets in the release

        Returns:
            Optional[str]: Description text if found, None otherwise
        """
        # Try to find a matching text file (e.g., video.webm -> video.txt)
        base_name = video_asset_name.rsplit('.', 1)[0]

        for ext in self.config.text_extensions:
            text_filename = base_name + ext
            if text_filename in assets:
                try:
                    text_url = assets[text_filename]
                    response = self.session.get(text_url, timeout=self.config.network_timeout)
                    response.raise_for_status()
                    return response.text
                except requests.RequestException as e:
                    logger.warning(f"Failed to fetch description for {video_asset_name}: {e}")
                    break  # Don't try other extensions if one fails

        return None

    def validate_repository_access(self) -> bool:
        """
        Validate that the configured repository is accessible.

        Returns:
            bool: True if repository is accessible, False otherwise
        """
        try:
            url = f"https://api.github.com/repos/{self.config.github_repo}"
            response = self.session.get(url, timeout=self.config.network_timeout)
            return response.status_code == 200
        except requests.RequestException:
            return False
