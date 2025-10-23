"""Tests for download service."""

import pytest
import requests
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open

from models.config import ApplicationConfig
from services.download_service import DownloadService


class TestDownloadService:
    """Test cases for DownloadService."""

    @pytest.fixture
    def download_service(self, sample_config):
        """Create a download service instance."""
        return DownloadService(sample_config)

    def test_initialization(self, sample_config):
        """Test download service initialization."""
        service = DownloadService(sample_config)

        assert service.config == sample_config
        assert service.session is not None

    def test_get_cached_asset_path(self, download_service, temp_cache_dir):
        """Test cache path generation."""
        download_service.config.cache_directory = temp_cache_dir

        path = download_service.get_cached_asset_path("video.webm")
        expected = temp_cache_dir / "video.webm"

        assert path == expected

    def test_is_asset_cached(self, download_service, temp_cache_dir):
        """Test asset cache checking."""
        download_service.config.cache_directory = temp_cache_dir

        # Test non-existent file
        assert download_service.is_asset_cached("nonexistent.webm") is False

        # Test existing file
        cached_file = temp_cache_dir / "existing.webm"
        cached_file.write_text("test content")

        assert download_service.is_asset_cached("existing.webm") is True

    @patch('services.download_service.requests.Session')
    def test_download_asset_success(self, mock_session_class, download_service, temp_cache_dir):
        """Test successful asset download."""
        download_service.config.cache_directory = temp_cache_dir

        # Setup mock response
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'content-length': '10'}
        mock_response.iter_content.return_value = [b'test', b' data']
        mock_response.raise_for_status.return_value = None
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        # Test download
        destination = temp_cache_dir / "test.webm"
        result = service.download_asset("https://example.com/test.webm", destination)

        assert result == destination
        assert destination.exists()
        assert destination.read_text() == "test data"

    @patch('services.download_service.requests.Session')
    def test_download_asset_already_exists(self, mock_session_class, download_service, temp_cache_dir):
        """Test download when file already exists."""
        download_service.config.cache_directory = temp_cache_dir

        # Create existing file
        existing_file = temp_cache_dir / "existing.webm"
        existing_file.write_text("existing content")

        mock_session_class.return_value = MagicMock()

        # Create service with mocked session
        service = DownloadService(download_service.config)

        # Test download of existing file
        result = service.download_asset("https://example.com/existing.webm", existing_file)

        assert result == existing_file
        # Session should not be used since file exists
        service.session.get.assert_not_called()

    @patch('services.download_service.requests.Session')
    def test_download_asset_with_progress_callback(self, mock_session_class, download_service, temp_cache_dir):
        """Test download with progress callback."""
        download_service.config.cache_directory = temp_cache_dir

        # Setup mock response
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'content-length': '100'}
        mock_response.iter_content.return_value = [b'x' * 50, b'x' * 50]
        mock_response.raise_for_status.return_value = None
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        # Test with progress callback
        progress_calls = []
        def progress_callback(downloaded, total):
            progress_calls.append((downloaded, total))

        destination = temp_cache_dir / "progress_test.webm"
        service.download_asset(
            "https://example.com/progress_test.webm",
            destination,
            progress_callback
        )

        # Check that progress callback was called
        assert len(progress_calls) > 0
        # Final call should show completion
        assert progress_calls[-1] == (100, 100)

    @patch('services.download_service.requests.Session')
    def test_download_asset_network_error(self, mock_session_class, download_service, temp_cache_dir):
        """Test download with network error."""
        download_service.config.cache_directory = temp_cache_dir

        # Setup mock to raise exception
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_response.raise_for_status.side_effect = Exception("Network error")
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        destination = temp_cache_dir / "error_test.webm"

        # Test that exception is raised
        with pytest.raises(Exception, match="Network error"):
            service.download_asset("https://example.com/error_test.webm", destination)

        # File should not exist after failed download
        assert not destination.exists()

    @patch('services.download_service.requests.Session')
    def test_get_download_size_success(self, mock_session_class, download_service):
        """Test getting download size successfully."""
        # Setup mock response
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'content-length': '12345'}
        mock_session.head.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        # Test size retrieval
        size = service.get_download_size("https://example.com/file.webm")

        assert size == 12345

    @patch('services.download_service.requests.Session')
    def test_get_download_size_no_content_length(self, mock_session_class, download_service):
        """Test getting download size when no content-length header."""
        # Setup mock response without content-length
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_session.head.return_value = mock_response
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        # Test size retrieval
        size = service.get_download_size("https://example.com/file.webm")

        assert size is None

    @patch('services.download_service.requests.Session')
    def test_get_download_size_error(self, mock_session_class, download_service):
        """Test getting download size with network error."""
        # Setup mock to raise exception
        mock_session = MagicMock()
        mock_session.head.side_effect = requests.RequestException("Connection failed")
        mock_session_class.return_value = mock_session

        # Create service with mocked session
        service = DownloadService(download_service.config)
        service.session = mock_session

        # Test size retrieval
        size = service.get_download_size("https://example.com/file.webm")

        assert size is None