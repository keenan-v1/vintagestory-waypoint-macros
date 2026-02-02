"""Reference image generation for waypoint macros."""

from __future__ import annotations

import platform
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

from PIL import Image, ImageDraw, ImageFont

from vs_waypoint_macros.models import KEYCODE_TO_NAME

if TYPE_CHECKING:
    from vs_waypoint_macros.models import Waypoint

# Image generation constants
KEY_SIZE = 80
KEY_MARGIN = 5
PADDING = 40
FONT_SIZE = 12
TITLE_FONT_SIZE = 16
BRIGHTNESS_THRESHOLD = 128
GRID_COLUMNS = 5

# Numpad layout (row, col) -> key name
NUMPAD_LAYOUT: list[list[str | None]] = [
    ["NUM", "/", "*", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", None],
    ["1", "2", "3", "Enter"],
    ["0", None, ".", None],
]


def _get_system_font() -> tuple[str, ...]:
    """Get appropriate font names for the current platform."""
    system = platform.system()
    if system == "Windows":
        return ("arial.ttf", "segoeui.ttf", "tahoma.ttf")
    elif system == "Darwin":  # macOS
        return (
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNSText.ttf",
            "/Library/Fonts/Arial.ttf",
        )
    else:  # Linux and others
        return (
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/TTF/DejaVuSans.ttf",
        )


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load a font, trying system fonts first then falling back to default."""
    for font_path in _get_system_font():
        try:
            return ImageFont.truetype(font_path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert a hex color string to RGB tuple."""
    return (
        int(hex_color[1:3], 16),
        int(hex_color[3:5], 16),
        int(hex_color[5:7], 16),
    )


def _get_text_color(background_hex: str) -> str:
    """Return black or white text color based on background brightness."""
    try:
        r, g, b = _hex_to_rgb(background_hex)
        # Standard luminance formula
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "#000000" if brightness > BRIGHTNESS_THRESHOLD else "#ffffff"
    except ValueError:
        return "#ffffff"


def _word_wrap(
    text: str,
    max_width: int,
    draw: ImageDraw.ImageDraw,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> list[str]:
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines: list[str] = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip() if current_line else word
        test_bbox = draw.textbbox((0, 0), test_line, font=font)
        test_width = test_bbox[2] - test_bbox[0]

        if test_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def _draw_numpad_key(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    width: int,
    height: int,
    key_name: str,
    fill_color: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    waypoint: Waypoint | None = None,
) -> None:
    """Draw a single numpad key."""
    # Draw key background
    draw.rounded_rectangle(
        [x, y, x + width, y + height],
        radius=5,
        fill=fill_color,
        outline="#606060",
    )

    text_color = _get_text_color(fill_color)

    # Draw key number at top, centered
    key_bbox = draw.textbbox((0, 0), key_name, font=font)
    key_text_width = key_bbox[2] - key_bbox[0]
    key_x = x + (width - key_text_width) // 2
    key_y = y + 5
    draw.text((key_x, key_y), key_name, fill=text_color, font=font)

    # Draw waypoint name below, word-wrapped
    if waypoint:
        lines = _word_wrap(waypoint.name, width - 10, draw, font)
        line_height = font.getbbox("A")[3] + 2
        name_start_y = key_y + line_height + 5

        for i, line in enumerate(lines):
            line_bbox = draw.textbbox((0, 0), line, font=font)
            line_width = line_bbox[2] - line_bbox[0]
            line_x = x + (width - line_width) // 2
            line_y = name_start_y + i * line_height
            draw.text((line_x, line_y), line, fill=text_color, font=font)


def generate_reference_image(
    waypoints: list[Waypoint],
    output_path: Path,
    *,
    verbose: bool = True,
) -> Path:
    """Generate a visual reference image of the numpad macro layout.

    Args:
        waypoints: List of waypoints to include in the reference.
        output_path: Path to save the generated image.
        verbose: Whether to print progress messages.

    Returns:
        Path to the generated image file.
    """
    # Group waypoints by category
    categories: dict[str, list[Waypoint]] = defaultdict(list)
    for wp in waypoints:
        categories[wp.category.name].append(wp)

    # Calculate image size
    grid_width = 4 * (KEY_SIZE + KEY_MARGIN)
    grid_height = 5 * (KEY_SIZE + KEY_MARGIN)

    rows = (len(categories) + GRID_COLUMNS - 1) // GRID_COLUMNS

    img_width = GRID_COLUMNS * (grid_width + PADDING * 2) + PADDING
    img_height = rows * (grid_height + PADDING * 3) + PADDING * 2

    # Create image
    img = Image.new("RGB", (img_width, img_height), "#2b2b2b")
    draw = ImageDraw.Draw(img)

    # Load fonts
    font = _load_font(FONT_SIZE)
    title_font = _load_font(TITLE_FONT_SIZE)

    # Draw each category's numpad
    for cat_idx, (cat_name, cat_waypoints) in enumerate(categories.items()):
        col = cat_idx % GRID_COLUMNS
        row = cat_idx // GRID_COLUMNS

        base_x = PADDING + col * (grid_width + PADDING * 2)
        base_y = PADDING + row * (grid_height + PADDING * 3)

        # Get category info
        category = cat_waypoints[0].category
        cat_key = KEYCODE_TO_NAME.get(category.key_code, "?")

        # Draw category title
        title = f"{cat_name} (NumPad {cat_key})"
        draw.text((base_x, base_y), title, fill="#ffffff", font=title_font)

        # Build waypoint lookup by key
        wp_by_key: dict[str, Waypoint] = {
            KEYCODE_TO_NAME.get(wp.key_code, "?"): wp for wp in cat_waypoints
        }

        # Draw numpad keys
        for row_idx, key_row in enumerate(NUMPAD_LAYOUT):
            for col_idx, key_name in enumerate(key_row):
                if key_name is None:
                    continue

                x = base_x + col_idx * (KEY_SIZE + KEY_MARGIN)
                y = base_y + TITLE_FONT_SIZE + 10 + row_idx * (KEY_SIZE + KEY_MARGIN)

                # Special handling for wide/tall keys
                width = KEY_SIZE
                height = KEY_SIZE
                if key_name == "0":
                    width = KEY_SIZE * 2 + KEY_MARGIN
                elif key_name == "+":
                    height = KEY_SIZE * 2 + KEY_MARGIN
                elif key_name == "Enter":
                    continue  # Skip Enter key

                # Determine key color and waypoint
                waypoint = wp_by_key.get(key_name)
                fill_color = waypoint.resolved_color if waypoint else "#404040"

                _draw_numpad_key(draw, x, y, width, height, key_name, fill_color, font, waypoint)

    # Save image
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)

    if verbose:
        print(f"Generated reference image: {output_path}")

    return output_path
