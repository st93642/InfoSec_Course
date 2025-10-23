"""Tests for playlist widget helper behaviour."""

from models.release_video import ReleaseVideo
from ui.playlist_widget import PlaylistWidget


def _make_video(seq: int) -> ReleaseVideo:
    """Create a simple ReleaseVideo for testing."""
    return ReleaseVideo(
        tag=f"1.0.{seq}",
        body="",
        asset_name=f"video{seq}.mp4",
        asset_url=f"https://example.com/video{seq}.mp4",
        text_url=None,
        description=f"Video {seq}",
    )


def test_get_next_video_returns_next(qtbot):
    widget = PlaylistWidget()
    qtbot.addWidget(widget)

    category = widget.add_category("Category")
    video1 = _make_video(1)
    video2 = _make_video(2)
    widget.add_video_to_category(category, video1)
    widget.add_video_to_category(category, video2)

    assert widget.get_next_video(video1) == video2


def test_get_next_video_returns_none_for_last_item(qtbot):
    widget = PlaylistWidget()
    qtbot.addWidget(widget)

    category = widget.add_category("Category")
    video1 = _make_video(1)
    widget.add_video_to_category(category, video1)

    assert widget.get_next_video(video1) is None


def test_get_next_video_unknown_video_returns_none(qtbot):
    widget = PlaylistWidget()
    qtbot.addWidget(widget)

    category = widget.add_category("Category")
    video1 = _make_video(1)
    widget.add_video_to_category(category, video1)

    assert widget.get_next_video(_make_video(99)) is None
