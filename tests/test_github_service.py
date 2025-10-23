"""Tests for GitHub service."""

import pytest
import requests
from unittest.mock import MagicMock, patch

from models.config import ApplicationConfig
from services.github_service import GitHubService


class TestGitHubService:
    """Test cases for GitHubService."""

    @pytest.fixture
    def github_service(self, sample_config):
        """Create a GitHub service instance."""
        return GitHubService(sample_config)

    def test_initialization(self, sample_config):
        """Test GitHub service initialization."""
        service = GitHubService(sample_config)

        assert service.config == sample_config
        assert service.session is not None

    def test_initialization_with_token(self, sample_config):
        """Test initialization with GitHub token."""
        sample_config.github_token = "test_token"
        service = GitHubService(sample_config)

        # Check that authorization header is set
        assert 'Authorization' in service.session.headers
        assert service.session.headers['Authorization'] == 'token test_token'

    @patch('services.github_service.requests.Session')
    def test_fetch_releases_success(self, mock_session_class, github_service, mock_github_response):
        """Test successful release fetching."""
        # Setup mock
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_github_response
        mock_response.raise_for_status.return_value = None
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        # Test fetching
        videos = service.fetch_releases()

        assert len(videos) == 1
        assert videos[0].tag == "v1.0.0"
        assert videos[0].asset_name == "video1.webm"

    @patch('services.github_service.requests.Session')
    def test_fetch_releases_with_tag_filter(self, mock_session_class, github_service, mock_github_response):
        """Test release fetching with tag filter."""
        # Add another release to mock response
        mock_github_response.append({
            "tag_name": "v2.0.0",
            "name": "Release v2.0.0",
            "body": "Release 2 description",
            "assets": [
                {
                    "name": "video2.webm",
                    "browser_download_url": "https://example.com/video2.webm"
                }
            ]
        })

        # Setup mock
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_github_response
        mock_response.raise_for_status.return_value = None
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        # Test fetching with tag filter
        videos = service.fetch_releases(tag="v1.0.0")

        assert len(videos) == 1
        assert videos[0].tag == "v1.0.0"

    @patch('services.github_service.requests.Session')
    def test_fetch_releases_network_error(self, mock_session_class, github_service):
        """Test handling of network errors."""
        # Setup mock to raise exception
        mock_session = MagicMock()
        mock_session.get.side_effect = Exception("Network error")
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        # Test that exception is raised
        with pytest.raises(Exception, match="Network error"):
            service.fetch_releases()

    def test_is_video_asset(self, github_service):
        """Test video asset detection."""
        assert github_service._is_video_asset("video.webm") is True
        assert github_service._is_video_asset("video.mp4") is True
        assert github_service._is_video_asset("video.avi") is True
        assert github_service._is_video_asset("document.txt") is False
        assert github_service._is_video_asset("image.jpg") is False

    @patch('services.github_service.requests.Session')
    def test_get_description_for_video(self, mock_session_class, github_service):
        """Test fetching description for video."""
        assets = {
            "video.webm": "https://example.com/video.webm",
            "video.txt": "https://example.com/video.txt"
        }

        # Setup mock for description fetch
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Video description"
        mock_response.raise_for_status.return_value = None
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        # Test description fetching
        description = service._get_description_for_video("video.webm", assets)

        assert description == "Video description"
        mock_session.get.assert_called_with("https://example.com/video.txt", timeout=30)

    @patch('services.github_service.requests.Session')
    def test_get_description_for_video_no_text_file(self, mock_session_class, github_service):
        """Test when no text file exists for video."""
        assets = {
            "video.webm": "https://example.com/video.webm"
        }

        mock_session_class.return_value = MagicMock()

        # Create service with mocked session
        service = GitHubService(github_service.config)

        # Test description fetching when no text file exists
        description = service._get_description_for_video("video.webm", assets)

        assert description is None

    @patch('services.github_service.requests.Session')
    def test_validate_repository_access_success(self, mock_session_class, github_service):
        """Test successful repository access validation."""
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        assert service.validate_repository_access() is True

    @patch('services.github_service.requests.Session')
    def test_validate_repository_access_failure(self, mock_session_class, github_service):
        """Test failed repository access validation."""
        mock_session = MagicMock()
        mock_session.get.side_effect = requests.RequestException("Connection failed")
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = GitHubService(github_service.config)
        service.session = mock_session

        assert service.validate_repository_access() is False