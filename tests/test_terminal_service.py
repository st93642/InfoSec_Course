"""Tests for terminal service."""

import subprocess
import pytest
from unittest.mock import MagicMock, patch

from models.config import ApplicationConfig
from services.terminal_service import TerminalService


class TestTerminalService:
    """Test cases for TerminalService."""

    @pytest.fixture
    def config(self):
        """Create a test configuration."""
        return ApplicationConfig()

    @pytest.fixture
    def terminal_service(self, config):
        """Create a terminal service instance."""
        return TerminalService(config)

    @patch('services.terminal_service.platform.system')
    @patch('services.terminal_service.subprocess.Popen')
    def test_embed_in_widget_linux_success(self, mock_popen, mock_platform_system, terminal_service):
        """Test successful terminal embedding on Linux."""
        mock_platform_system.return_value = "Linux"

        # Mock successful process creation
        mock_process = MagicMock()
        mock_popen.return_value = mock_process

        widget_win_id = 12345
        geometry = "80x24"

        result = terminal_service.embed_in_widget(widget_win_id, geometry)

        assert result is True
        assert terminal_service.is_embedded is True
        assert terminal_service.widget_win_id == widget_win_id

        # Check subprocess call
        mock_popen.assert_called_with([
            "xterm", 
            "-into", str(widget_win_id), 
            "-geometry", geometry,
            "-fa", "Monospace-14",
            "-fs", "14"
        ])

    @patch('services.terminal_service.platform.system')
    def test_embed_in_widget_non_linux(self, mock_platform_system, terminal_service):
        """Test terminal embedding on non-Linux platform."""
        mock_platform_system.return_value = "Windows"

        widget_win_id = 12345

        result = terminal_service.embed_in_widget(widget_win_id)

        assert result is False
        assert terminal_service.is_embedded is False

    @patch('services.terminal_service.platform.system')
    @patch('services.terminal_service.subprocess.Popen')
    def test_embed_in_widget_subprocess_error(self, mock_popen, mock_platform_system, terminal_service):
        """Test terminal embedding with subprocess error."""
        mock_platform_system.return_value = "Linux"
        mock_popen.side_effect = OSError("Command not found")

        widget_win_id = 12345

        result = terminal_service.embed_in_widget(widget_win_id)

        assert result is False
        assert terminal_service.is_embedded is False

    @patch('services.terminal_service.subprocess.Popen')
    def test_launch_external_terminal_success(self, mock_popen, terminal_service):
        """Test successful external terminal launch."""
        mock_process = MagicMock()
        mock_popen.return_value = mock_process

        result = terminal_service.launch_external_terminal()

        assert result is True
        assert terminal_service.is_embedded is False
        mock_popen.assert_called_with(["xterm"])

    @patch('services.terminal_service.subprocess.Popen')
    def test_launch_external_terminal_error(self, mock_popen, terminal_service):
        """Test external terminal launch with error."""
        mock_popen.side_effect = OSError("Command not found")

        result = terminal_service.launch_external_terminal()

        assert result is False

    def test_update_geometry_embedded(self, terminal_service):
        """Test geometry update for embedded terminal."""
        # Set up embedded terminal
        terminal_service.is_embedded = True
        terminal_service.widget_win_id = 12345

        # This should not raise an exception
        terminal_service.update_geometry(800, 600)

        # Note: Actual geometry update logic is minimal in current implementation

    def test_update_geometry_not_embedded(self, terminal_service):
        """Test geometry update for non-embedded terminal."""
        terminal_service.is_embedded = False

        # Should not do anything
        terminal_service.update_geometry(800, 600)

    def test_get_recommended_geometry(self, terminal_service):
        """Test geometry calculation."""
        geometry = terminal_service.get_recommended_geometry(800, 600)

        # Should return a geometry string
        assert isinstance(geometry, str)
        assert "x" in geometry

        # Parse geometry
        cols, rows = geometry.split("x")
        cols, rows = int(cols), int(rows)

        # Check reasonable bounds
        assert cols >= 80
        assert rows >= 24

    def test_is_running_no_process(self, terminal_service):
        """Test running check when no process exists."""
        assert terminal_service.is_running() is False

    def test_is_running_process_alive(self, terminal_service):
        """Test running check when process is alive."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None  # Process still running
        terminal_service.process = mock_process

        assert terminal_service.is_running() is True

    def test_is_running_process_dead(self, terminal_service):
        """Test running check when process is dead."""
        mock_process = MagicMock()
        mock_process.poll.return_value = 0  # Process finished
        terminal_service.process = mock_process

        assert terminal_service.is_running() is False

    def test_send_signal_running_process(self, terminal_service):
        """Test sending signal to running process."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None
        terminal_service.process = mock_process

        signal_num = 15  # SIGTERM

        terminal_service.send_signal(signal_num)

        mock_process.send_signal.assert_called_with(signal_num)

    def test_send_signal_no_process(self, terminal_service):
        """Test sending signal when no process exists."""
        terminal_service.send_signal(15)

        # Should not raise exception

    def test_send_signal_process_error(self, terminal_service):
        """Test sending signal with process error."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None
        mock_process.send_signal.side_effect = OSError("Permission denied")
        terminal_service.process = mock_process

        # Should not raise exception
        terminal_service.send_signal(15)

    def test_cleanup_no_process(self, terminal_service):
        """Test cleanup when no process exists."""
        terminal_service.cleanup()

        # Should not raise exception
        assert terminal_service.process is None
        assert terminal_service.is_embedded is False
        assert terminal_service.widget_win_id is None

    def test_cleanup_running_process(self, terminal_service):
        """Test cleanup of running process."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None
        terminal_service.process = mock_process
        terminal_service.is_embedded = True
        terminal_service.widget_win_id = 12345

        terminal_service.cleanup()

        # Process should be terminated
        mock_process.terminate.assert_called_once()
        mock_process.wait.assert_called_once()

        # State should be reset
        assert terminal_service.process is None
        assert terminal_service.is_embedded is False
        assert terminal_service.widget_win_id is None

    def test_cleanup_process_terminate_timeout(self, terminal_service):
        """Test cleanup when process doesn't terminate gracefully."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None
        mock_process.wait.side_effect = subprocess.TimeoutExpired(cmd=[], timeout=2.0)
        terminal_service.process = mock_process

        terminal_service.cleanup()

        # Should try to terminate then kill
        mock_process.terminate.assert_called_once()
        mock_process.kill.assert_called_once()

    def test_cleanup_error(self, terminal_service):
        """Test cleanup with errors."""
        mock_process = MagicMock()
        mock_process.poll.return_value = None
        mock_process.terminate.side_effect = Exception("Terminate failed")
        terminal_service.process = mock_process

        # Should not raise exception
        terminal_service.cleanup()

        # State should still be reset
        assert terminal_service.process is None