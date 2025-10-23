"""Integration tests for the Video Terminal application."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from models.config import ApplicationConfig
from services.github_service import GitHubService
from services.download_service import DownloadService


@pytest.mark.integration
class TestServiceIntegration:
    """Integration tests for service interactions."""

    @pytest.fixture
    def config(self, temp_cache_dir):
        """Create test configuration."""
        config = ApplicationConfig()
        config.cache_directory = temp_cache_dir
        return config

    @patch('services.github_service.requests.Session')
    def test_github_and_download_integration(self, mock_session_class, config):
        """Test integration between GitHub service and download service."""
        # Mock GitHub API response
        mock_github_session = MagicMock()
        mock_github_response = MagicMock()
        mock_github_response.status_code = 200
        mock_github_response.json.return_value = [
            {
                "tag_name": "v1.0.0",
                "name": "Release v1.0.0",
                "body": "Test release",
                "assets": [
                    {
                        "name": "test.webm",
                        "browser_download_url": "https://example.com/test.webm"
                    },
                    {
                        "name": "test.txt",
                        "browser_download_url": "https://example.com/test.txt"
                    }
                ]
            }
        ]
        mock_github_response.raise_for_status.return_value = None

        # Mock text description response
        mock_text_response = MagicMock()
        mock_text_response.status_code = 200
        mock_text_response.text = "Video description"
        mock_text_response.raise_for_status.return_value = None

        # Set up GitHub session to return different responses based on URL
        def github_get_side_effect(url, **kwargs):
            if 'releases' in url:
                return mock_github_response
            elif url.endswith('.txt'):
                return mock_text_response
            else:
                return mock_github_response  # fallback

        mock_github_session.get.side_effect = github_get_side_effect

        # Mock download response
        mock_download_session = MagicMock()
        mock_download_response = MagicMock()
        mock_download_response.status_code = 200
        mock_download_response.headers = {'content-length': '100'}
        mock_download_response.iter_content.return_value = [b'test content']
        mock_download_response.raise_for_status.return_value = None
        mock_download_response.__enter__.return_value = mock_download_response
        mock_download_response.__exit__.return_value = None
        mock_download_session.get.return_value = mock_download_response

        def mock_session_factory():
            if mock_session_class.call_count == 1:
                return mock_github_session
            else:
                return mock_download_session

        mock_session_class.side_effect = mock_session_factory

        # Create services
        github_service = GitHubService(config)
        download_service = DownloadService(config)

        # Test full flow: fetch releases -> download video
        videos = github_service.fetch_releases()

        assert len(videos) == 1
        video = videos[0]

        assert video.tag == "v1.0.0"
        assert video.asset_name == "test.webm"
        assert video.description == "Video description"

        # Test download
        cache_path = download_service.get_cached_asset_path(video.asset_name)
        downloaded_path = download_service.download_asset(video.asset_url, cache_path)

        assert downloaded_path == cache_path
        assert downloaded_path.exists()
        assert downloaded_path.read_text() == "test content"

    def test_config_cache_directory_integration(self, config):
        """Test configuration and cache directory integration."""
        # Ensure cache directory is created
        config.ensure_cache_directory_exists()
        assert config.cache_directory.exists()

        # Test cache path generation
        asset_path = config.get_cache_path_for_asset("video.webm")
        assert asset_path.parent == config.cache_directory
        assert asset_path.name == "video.webm"

        # Test download service integration
        download_service = DownloadService(config)
        service_path = download_service.get_cached_asset_path("video.webm")

        assert service_path == asset_path