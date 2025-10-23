"""Tests for video service."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from services.video_service import VideoService, VLC_AVAILABLE


class TestVideoService:
    """Test cases for VideoService."""

    @pytest.fixture
    def video_service(self):
        """Create a video service instance."""
        with patch('services.video_service.vlc') as mock_vlc:
            # Mock VLC components
            mock_instance = MagicMock()
            mock_player = MagicMock()
            mock_instance.media_player_new.return_value = mock_player
            mock_vlc.Instance.return_value = mock_instance

            service = VideoService()
            return service

    def test_initialization_vlc_available(self):
        """Test initialization when VLC is available."""
        with patch('services.video_service.VLC_AVAILABLE', True), \
             patch('services.video_service.vlc') as mock_vlc:

            mock_instance = MagicMock()
            mock_player = MagicMock()
            mock_instance.media_player_new.return_value = mock_player
            mock_vlc.Instance.return_value = mock_instance

            service = VideoService()

            assert service.instance == mock_instance
            assert service.player == mock_player
            assert service.is_embedded is False

    def test_initialization_vlc_unavailable(self):
        """Test initialization when VLC is not available."""
        with patch('services.video_service.VLC_AVAILABLE', False):
            with pytest.raises(RuntimeError, match="VLC is not available"):
                VideoService()

    @patch('services.video_service.platform.system')
    def test_embed_in_widget_linux(self, mock_platform_system, video_service):
        """Test embedding video in widget on Linux."""
        mock_platform_system.return_value = "Linux"

        # Mock widget win_id
        widget_win_id = 12345

        result = video_service.embed_in_widget(widget_win_id)

        assert result is True
        assert video_service.is_embedded is True
        video_service.player.set_xwindow.assert_called_with(widget_win_id)

    @patch('services.video_service.platform.system')
    def test_embed_in_widget_non_linux(self, mock_platform_system, video_service):
        """Test embedding video in widget on non-Linux platform."""
        mock_platform_system.return_value = "Windows"

        widget_win_id = 12345

        result = video_service.embed_in_widget(widget_win_id)

        assert result is False
        assert video_service.is_embedded is False
        video_service.player.set_xwindow.assert_not_called()

    def test_load_video_success(self, video_service, tmp_path):
        """Test successful video loading."""
        video_file = tmp_path / "test.webm"
        video_file.write_text("fake video content")

        # Mock successful media creation
        mock_media = MagicMock()
        video_service.instance.media_new.return_value = mock_media

        result = video_service.load_video(video_file)

        assert result is True
        video_service.instance.media_new.assert_called_with(str(video_file))
        video_service.player.set_media.assert_called_with(mock_media)

    def test_load_video_file_not_exists(self, video_service, tmp_path):
        """Test loading non-existent video file."""
        non_existent_file = tmp_path / "nonexistent.webm"

        result = video_service.load_video(non_existent_file)

        assert result is False
        video_service.instance.media_new.assert_not_called()

    def test_load_video_error(self, video_service, tmp_path):
        """Test video loading with error."""
        video_file = tmp_path / "test.webm"
        video_file.write_text("fake video content")

        # Mock media creation to raise exception
        video_service.instance.media_new.side_effect = Exception("VLC error")

        result = video_service.load_video(video_file)

        assert result is False

    def test_play_success(self, video_service):
        """Test successful playback start."""
        video_service.player.play.return_value = 0  # VLC success code

        result = video_service.play()

        assert result is True
        video_service.player.play.assert_called_once()

    def test_play_failure(self, video_service):
        """Test playback start failure."""
        video_service.player.play.return_value = -1  # VLC error code

        result = video_service.play()

        assert result is False

    def test_pause(self, video_service):
        """Test video pause."""
        video_service.pause()

        video_service.player.pause.assert_called_once()

    def test_stop(self, video_service):
        """Test video stop."""
        video_service.stop()

        video_service.player.stop.assert_called_once()

    def test_set_position(self, video_service):
        """Test setting playback position."""
        position = 0.5

        video_service.set_position(position)

        video_service.player.set_position.assert_called_with(position)

    def test_get_position(self, video_service):
        """Test getting playback position."""
        expected_position = 0.75
        video_service.player.get_position.return_value = expected_position

        position = video_service.get_position()

        assert position == expected_position
        video_service.player.get_position.assert_called_once()

    def test_get_position_error(self, video_service):
        """Test getting position with error."""
        video_service.player.get_position.side_effect = Exception("VLC error")

        position = video_service.get_position()

        assert position == 0.0

    def test_set_volume(self, video_service):
        """Test setting volume."""
        volume = 75

        video_service.set_volume(volume)

        video_service.player.audio_set_volume.assert_called_with(volume)

    def test_get_length(self, video_service):
        """Test getting video length."""
        expected_length = 3600000  # 1 hour in milliseconds
        video_service.player.get_length.return_value = expected_length

        length = video_service.get_length()

        assert length == expected_length

    def test_get_length_error(self, video_service):
        """Test getting length with error."""
        video_service.player.get_length.side_effect = Exception("VLC error")

        length = video_service.get_length()

        assert length == 0

    def test_get_time(self, video_service):
        """Test getting current playback time."""
        expected_time = 1800000  # 30 minutes in milliseconds
        video_service.player.get_time.return_value = expected_time

        time = video_service.get_time()

        assert time == expected_time

    def test_set_time(self, video_service):
        """Test setting playback time."""
        time_ms = 900000  # 15 minutes

        video_service.set_time(time_ms)

        video_service.player.set_time.assert_called_with(time_ms)

    def test_is_playing(self, video_service):
        """Test checking if video is playing."""
        video_service.player.is_playing.return_value = True

        playing = video_service.is_playing()

        assert playing is True

    def test_is_playing_error(self, video_service):
        """Test checking play state with error."""
        video_service.player.is_playing.side_effect = Exception("VLC error")

        playing = video_service.is_playing()

        assert playing is False

    def test_cleanup(self, video_service):
        """Test service cleanup."""
        video_service.cleanup()

        video_service.player.stop.assert_called_once()