"""Text content widget for displaying release information and descriptions."""

import html
import logging
import re
from typing import Optional

from PyQt5 import QtWidgets

logger = logging.getLogger(__name__)


class TextContentWidget(QtWidgets.QTextEdit):
    """
    Widget for displaying text content from GitHub releases.

    This widget shows release descriptions, bodies, and other text content
    with support for both plain text and HTML rendering.
    """

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        """
        Initialize the text content widget.

        Args:
            parent (Optional[QWidget]): Parent widget
        """
        super().__init__(parent)

        # Configure as read-only text display
        self.setReadOnly(True)
        self.setAcceptRichText(True)

        # Configure appearance
        self.setStyleSheet("""
            QTextEdit {
                background-color: black;
                color: lime;
                border: 1px solid #333;
                font-family: monospace;
                font-size: 10pt;
            }
        """)

        # Set size policy
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Set placeholder text
        self.setPlaceholderText("Select a video to view its description...")

    def _is_html_content(self, content: str) -> bool:
        """
        Check if content appears to be HTML.

        Args:
            content (str): Content to check

        Returns:
            bool: True if content appears to be HTML
        """
        # Check for common HTML tags
        html_patterns = [
            r'<[^>]+>',  # Any HTML tag
            r'&[a-zA-Z]+;',  # HTML entities
            r'<html',  # HTML document start
            r'<!DOCTYPE',  # DOCTYPE declaration
        ]

        return any(re.search(pattern, content, re.IGNORECASE) for pattern in html_patterns)

    def _is_markdown_content(self, content: str) -> bool:
        """
        Check if content appears to be Markdown.

        Args:
            content (str): Content to check

        Returns:
            bool: True if content appears to be Markdown
        """
        # Check for common Markdown patterns
        markdown_patterns = [
            r'^#{1,6}\s+',  # Headers
            r'\*\*.*?\*\*',  # Bold text
            r'\*.*?\*',  # Italic text
            r'`.*?`',  # Inline code
            r'^\s*[-*+]\s+',  # List items
            r'^\s*\d+\.\s+',  # Numbered list items
            r'^\s*>\s+',  # Blockquotes
            r'^\s*```',  # Code blocks
            r'\[.*?\]\(.*?\)',  # Links
            r'!\[.*?\]\(.*?\)',  # Images
        ]

        return any(re.search(pattern, content, re.MULTILINE) for pattern in markdown_patterns)

    def _markdown_to_html(self, content: str) -> str:
        """
        Convert basic Markdown to HTML.

        Args:
            content (str): Markdown content

        Returns:
            str: HTML content
        """
        # Basic Markdown to HTML conversion
        lines = content.split('\n')
        html_lines = []
        in_code_block = False
        code_block_lang = ''

        for line in lines:
            # Code blocks
            if line.strip().startswith('```'):
                if in_code_block:
                    html_lines.append('</code></pre>')
                    in_code_block = False
                    code_block_lang = ''
                else:
                    in_code_block = True
                    code_block_lang = line.strip()[3:]
                    html_lines.append(f'<pre><code class="language-{code_block_lang}">')
                continue

            if in_code_block:
                html_lines.append(html.escape(line))
                continue

            # Headers
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if header_match:
                level = len(header_match.group(1))
                text = header_match.group(2)
                html_lines.append(f'<h{level}>{html.escape(text)}</h{level}>')
                continue

            # Bold and italic
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)

            # Inline code
            line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)

            # Links
            line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)

            # Lists
            if re.match(r'^\s*[-*+]\s+', line):
                line = re.sub(r'^\s*[-*+]\s+', '<li>', line) + '</li>'
                if not html_lines or not html_lines[-1].startswith('<ul>'):
                    html_lines.append('<ul>')
                html_lines.append(line)
                continue
            elif re.match(r'^\s*\d+\.\s+', line):
                line = re.sub(r'^\s*\d+\.\s+', '<li>', line) + '</li>'
                if not html_lines or not html_lines[-1].startswith('<ol>'):
                    html_lines.append('<ol>')
                html_lines.append(line)
                continue

            # Regular paragraphs
            if line.strip():
                html_lines.append(f'<p>{html.escape(line)}</p>')
            else:
                html_lines.append('<br>')

        # Close any open lists
        if html_lines and ('<ul>' in html_lines[-1] or '<ol>' in html_lines[-1]):
            html_lines.append('</ul>' if '<ul>' in html_lines[-1] else '</ol>')

        return '\n'.join(html_lines)

    def set_content(self, content: str, is_html: bool = False) -> None:
        """
        Set the text content to display.

        Args:
            content (str): The content to display
            is_html (bool): Whether the content is HTML (default: False, auto-detect)
        """
        if not content or not content.strip():
            self.setPlaceholderText("No description available for this video.")
            self.clear()
            return

        try:
            # Auto-detect content type if not specified
            if not is_html:
                if self._is_html_content(content):
                    is_html = True
                elif self._is_markdown_content(content):
                    # Convert markdown to HTML
                    content = self._markdown_to_html(content)
                    is_html = True

            if is_html:
                # Decode HTML entities before setting HTML content
                content = html.unescape(content)
                self.setHtml(content)
            else:
                # Plain text
                self.setPlainText(content)

            logger.debug(f"Set content ({len(content)} characters, HTML: {is_html})")
            logger.info(f"Text widget content set to: '{content[:50]}...' (visible: {self.isVisible()}, has content: {self.has_content()})")

        except Exception as e:
            logger.error(f"Error setting content: {e}")
            self.setPlainText(f"Error displaying content: {e}")

    def clear_content(self) -> None:
        """Clear the displayed content."""
        self.clear()
        self.setPlaceholderText("Select a video to view its description...")

    def set_font_size(self, size: int) -> None:
        """
        Set the font size for the text display.

        Args:
            size (int): Font size in points
        """
        font = self.font()
        font.setPointSize(size)
        self.setFont(font)

    def set_theme_colors(self, background: str = "black", foreground: str = "lime") -> None:
        """
        Set the color theme for the widget.

        Args:
            background (str): Background color (CSS color name or hex)
            foreground (str): Foreground/text color (CSS color name or hex)
        """
        self.setStyleSheet(f"""
            QTextEdit {{
                background-color: {background};
                color: {foreground};
                border: 1px solid #333;
                font-family: monospace;
                font-size: 10pt;
            }}
        """)

    def get_content_length(self) -> int:
        """
        Get the length of the currently displayed content.

        Returns:
            int: Number of characters in the content
        """
        return len(self.toPlainText())

    def has_content(self) -> bool:
        """
        Check if the widget currently has content displayed.

        Returns:
            bool: True if content is displayed
        """
        return self.get_content_length() > 0
