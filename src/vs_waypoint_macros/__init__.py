"""Vintage Story Waypoint Macro Generator.

Generate waypoint macros for Vintage Story using numpad key combinations.
"""

from vs_waypoint_macros.generator import generate_macros
from vs_waypoint_macros.image import generate_reference_image
from vs_waypoint_macros.models import Category, Icon, KeyCode, Waypoint

__version__ = "1.0.0"
__all__ = [
    "Category",
    "Icon",
    "KeyCode",
    "Waypoint",
    "generate_macros",
    "generate_reference_image",
]
