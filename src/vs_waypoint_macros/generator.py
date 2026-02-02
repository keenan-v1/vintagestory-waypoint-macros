"""Macro file generation for Vintage Story."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vs_waypoint_macros.models import Waypoint

# Default starting index for macro files
DEFAULT_START_INDEX = 100


def generate_macro(index: int, waypoint: Waypoint) -> dict[str, object]:
    """Generate a macro dictionary for a waypoint.

    Args:
        index: The macro index number.
        waypoint: The waypoint to generate a macro for.

    Returns:
        A dictionary representing the macro configuration.
    """
    macro_name = f"Waypoint {waypoint.category.name} {waypoint.name}"
    return {
        "Index": index,
        "Code": waypoint.name,
        "Name": macro_name,
        "Commands": [
            f"/waypoint addati {waypoint.resolved_icon} ~0 ~0 ~0 false "
            f"{waypoint.resolved_color} {waypoint.name}"
        ],
        "KeyCombination": {
            "KeyCode": waypoint.key_code.value,
            "SecondKeyCode": waypoint.category.key_code.value,
            "Ctrl": False,
            "Alt": False,
            "Shift": False,
            "OnKeyUp": False,
        },
    }


def generate_macros(
    waypoints: list[Waypoint],
    output_dir: Path,
    start_index: int = DEFAULT_START_INDEX,
    *,
    verbose: bool = True,
) -> list[Path]:
    """Generate all macro JSON files.

    Args:
        waypoints: List of waypoints to generate macros for.
        output_dir: Directory to write macro files to.
        start_index: Starting index for macro numbering.
        verbose: Whether to print progress messages.

    Returns:
        List of paths to generated files.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generated_files: list[Path] = []

    for i, waypoint in enumerate(waypoints):
        index = start_index + i
        macro = generate_macro(index, waypoint)
        filename = f"{index}-{macro['Name']}.json"
        filepath = output_dir / filename

        filepath.write_text(json.dumps(macro, indent=2), encoding="utf-8")

        if verbose:
            print(f"Generated: {filename}")

        generated_files.append(filepath)

    return generated_files
