"""Shared test fixtures and configuration."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock

from models.config import ApplicationConfig
from models.release_video import ReleaseVideo


@pytest.fixture
def temp_cache_dir(tmp_path):
    """Create a temporary cache directory."""
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    return cache_dir


@pytest.fixture
def sample_config(temp_cache_dir):
    """Create a sample application configuration."""
    config = ApplicationConfig()
    config.cache_directory = temp_cache_dir
    return config


@pytest.fixture
def sample_release_video():
    """Create a sample ReleaseVideo instance."""
    return ReleaseVideo(
        tag="v1.0.0",
        body="Sample release description",
        asset_name="sample_video.webm",
        asset_url="https://example.com/sample_video.webm",
        description="Sample video description"
    )


@pytest.fixture
def mock_github_response():
    """Mock GitHub API response for releases."""
    return [
        {
            "tag_name": "v1.0.0",
            "name": "Release v1.0.0",
            "body": "Release description",
            "assets": [
                {
                    "name": "video1.webm",
                    "browser_download_url": "https://example.com/video1.webm"
                },
                {
                    "name": "video1.txt",
                    "browser_download_url": "https://example.com/video1.txt"
                }
            ]
        }
    ]


@pytest.fixture
def mock_requests_session():
    """Mock requests session for testing."""
    session = MagicMock()
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = []
    response.headers = {'content-length': '1000'}
    response.iter_content.return_value = [b'chunk1', b'chunk2']
    response.raise_for_status.return_value = None
    session.get.return_value.__enter__.return_value = response
    session.head.return_value = response
    return session