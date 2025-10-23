"""Tests for data models."""

import pytest
from pathlib import Path

from models.config import ApplicationConfig
from models.release_video import ReleaseVideo


class TestReleaseVideo:
    """Test cases for ReleaseVideo model."""

    def test_release_video_creation(self):
        """Test basic ReleaseVideo creation."""
        video = ReleaseVideo(
            tag="v1.0.0",
            body="Release body",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm",
            description="Video description"
        )

        assert video.tag == "v1.0.0"
        assert video.body == "Release body"
        assert video.asset_name == "video.webm"
        assert video.asset_url == "https://example.com/video.webm"
        assert video.description == "Video description"

    def test_release_video_display_name(self):
        """Test display name property."""
        video = ReleaseVideo(
            tag="v1.0.0",
            body="",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm"
        )

        assert video.display_name == "v1.0.0 — video.webm"

    def test_release_video_has_description(self):
        """Test has_description property."""
        video_with_desc = ReleaseVideo(
            tag="v1.0.0",
            body="",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm",
            description="Description"
        )

        video_without_desc = ReleaseVideo(
            tag="v1.0.0",
            body="",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm"
        )

        video_empty_desc = ReleaseVideo(
            tag="v1.0.0",
            body="",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm",
            description=""
        )

        assert video_with_desc.has_description is True
        assert video_without_desc.has_description is False
        assert video_empty_desc.has_description is False

    def test_release_video_get_content_text(self):
        """Test get_content_text method."""
        video_with_desc = ReleaseVideo(
            tag="v1.0.0",
            body="Release body",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm",
            description="Video description"
        )

        video_without_desc = ReleaseVideo(
            tag="v1.0.0",
            body="Release body",
            asset_name="video.webm",
            asset_url="https://example.com/video.webm"
        )

        assert video_with_desc.get_content_text() == "Video description"
        assert video_without_desc.get_content_text() == "Release body"


class TestApplicationConfig:
    """Test cases for ApplicationConfig."""

    def test_default_config(self):
        """Test default configuration values."""
        config = ApplicationConfig()

        assert config.github_repo == "st93642/Assets"
        assert config.github_token is None
        assert config.cache_directory == Path.home() / "Downloads"
        assert config.video_extensions == (".webm", ".mp4", ".avi", ".mkv")
        assert config.text_extensions == (".txt", ".md")
        assert config.network_timeout == 30
        assert config.download_chunk_size == 8192

    def test_config_from_environment(self, monkeypatch, temp_cache_dir):
        """Test configuration from environment variables."""
        monkeypatch.setenv('GITHUB_REPO', 'test/repo')
        monkeypatch.setenv('GITHUB_TOKEN', 'test_token')
        monkeypatch.setenv('CACHE_DIR', str(temp_cache_dir))

        config = ApplicationConfig.from_environment()

        assert config.github_repo == 'test/repo'
        assert config.github_token == 'test_token'
        assert config.cache_directory == temp_cache_dir

    def test_ensure_cache_directory_exists(self, tmp_path):
        """Test cache directory creation."""
        config = ApplicationConfig()
        config.cache_directory = tmp_path / "test_cache"

        assert not config.cache_directory.exists()
        config.ensure_cache_directory_exists()
        assert config.cache_directory.exists()
        assert config.cache_directory.is_dir()

    def test_get_cache_path_for_asset(self, temp_cache_dir):
        """Test cache path generation for assets."""
        config = ApplicationConfig()
        config.cache_directory = temp_cache_dir

        path = config.get_cache_path_for_asset("video.webm")
        expected = temp_cache_dir / "video.webm"

        assert path == expected