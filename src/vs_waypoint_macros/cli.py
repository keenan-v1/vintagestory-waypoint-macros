"""Command-line interface for vs-waypoint-macros."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from vs_waypoint_macros.generator import DEFAULT_START_INDEX, generate_macros
from vs_waypoint_macros.image import generate_reference_image
from vs_waypoint_macros.waypoints import WAYPOINTS


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="vs-waypoint-macros",
        description="Generate waypoint macros for Vintage Story with visual numpad reference.",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path.cwd(),
        help="Output directory for generated files (default: current directory)",
    )

    parser.add_argument(
        "-s",
        "--start-index",
        type=int,
        default=DEFAULT_START_INDEX,
        help=f"Starting index for macro numbering (default: {DEFAULT_START_INDEX})",
    )

    parser.add_argument(
        "--macros-only",
        action="store_true",
        help="Only generate macro files, skip reference image",
    )

    parser.add_argument(
        "--image-only",
        action="store_true",
        help="Only generate reference image, skip macro files",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress output messages",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )

    return parser.parse_args(args)


def main(args: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parsed = parse_args(args)
    verbose = not parsed.quiet

    output_dir = Path(parsed.output).resolve()

    if parsed.macros_only and parsed.image_only:
        print("Error: Cannot specify both --macros-only and --image-only", file=sys.stderr)
        return 1

    try:
        # Generate macro files
        if not parsed.image_only:
            files = generate_macros(
                WAYPOINTS,
                output_dir,
                start_index=parsed.start_index,
                verbose=verbose,
            )
            if verbose:
                count = len(files)
                print(f"\nGenerated {count} macro files starting at index {parsed.start_index}")

        # Generate reference image
        if not parsed.macros_only:
            image_path = output_dir / "macro-reference.png"
            generate_reference_image(WAYPOINTS, image_path, verbose=verbose)

    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
