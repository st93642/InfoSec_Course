"""Data models for the Video Terminal application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ReleaseVideo:
    """
    Represents a video asset from a GitHub release.

    This class encapsulates information about a video file associated with a GitHub release,
    including metadata and download information.

    Attributes:
        tag (str): The release tag name (e.g., "v1.0.0")
        body (str): The release body/description in Markdown format
        asset_name (str): The filename of the video asset (e.g., "video.webm")
        asset_url (str): The download URL for the video asset
        text_url (str): Optional download URL for the paired .txt description file
        description (str): Optional text description from a paired .txt file
    """
    tag: str
    body: str
    asset_name: str
    asset_url: str
    text_url: Optional[str] = None
    description: Optional[str] = None
    _display_name: Optional[str] = None  # Custom display name for clean presentation

    @property
    def display_name(self) -> str:
        """Get a display-friendly name for the video."""
        if self._display_name:
            return self._display_name
        return f"{self.tag} — {self.asset_name}"

    @property
    def has_description(self) -> bool:
        """Check if this video has a text description."""
        return self.description is not None and len(self.description.strip()) > 0

    def get_content_text(self) -> str:
        """Get the content text to display (description if available, otherwise body)."""
        return self.description if self.has_description else self.body
