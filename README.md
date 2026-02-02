# Vintage Story Waypoint Macros

Generate waypoint macros for [Vintage Story](https://www.vintagestory.at/) using numpad key combinations.

This tool creates macro files that let you quickly place waypoints in-game using a two-key numpad system:
- First key selects the category (POI, Metals, Grains, etc.)
- Second key selects the specific waypoint within that category

It also generates a visual reference image showing all keybindings.

## Quick Start (Pre-generated Macros)

If you just want the macros without installing anything:

1. Download `vintagestory-waypoint-macros.zip` from the [Releases](https://github.com/keenan-v1/vintagestory-waypoint-macros/releases/latest) page
2. Extract the `.json` files to your Vintage Story macros folder:
   - **Windows:** `%appdata%\VintagestoryData\Macros\`
   - **Linux:** `~/.config/VintagestoryData/Macros/`
   - **macOS:** `~/Library/Application Support/VintagestoryData/Macros/`
3. Restart Vintage Story

The release also includes `macro-reference.png` - a visual guide to all keybindings.

## Installation (Optional)

Only needed if you want to customize waypoints or regenerate macros:

```bash
git clone https://github.com/keenan-v1/vintagestory-waypoint-macros.git
cd vintagestory-waypoint-macros
pip install .
```

## Usage

### Command Line

Generate macros in the current directory:

```bash
vs-waypoint-macros
```

Specify an output directory:

```bash
vs-waypoint-macros -o /path/to/output
```

Generate only macro files (no reference image):

```bash
vs-waypoint-macros --macros-only
```

Generate only the reference image:

```bash
vs-waypoint-macros --image-only
```

### As a Python Module

```bash
python -m vs_waypoint_macros
```

### Programmatic Usage

```python
from pathlib import Path
from vs_waypoint_macros import generate_macros, generate_reference_image
from vs_waypoint_macros.waypoints import WAYPOINTS

output_dir = Path("./macros")
generate_macros(WAYPOINTS, output_dir)
generate_reference_image(WAYPOINTS, output_dir / "reference.png")
```

## Generating Custom Macros

1. Run `vs-waypoint-macros -o <output_directory>`
2. Copy the generated `.json` files to your Vintage Story macros folder (see paths in Quick Start above)
3. Restart Vintage Story

## Categories

| NumPad Key | Category      |
|------------|---------------|
| 0          | POI           |
| 1          | Metals        |
| 2          | Minerals      |
| 3          | Grains        |
| 4          | Crops         |
| 5          | Mushrooms     |
| 6          | Berries       |
| 7          | Trees (Warm)  |
| 8          | Trees (Cold)  |
| 9          | Resources     |

## Development

Install with development dependencies:

```bash
pip install -e ".[dev]"
```

Run linting:

```bash
ruff check src/
ruff format src/
```

## License

MIT
