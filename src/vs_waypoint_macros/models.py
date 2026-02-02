"""Data models for waypoint macros."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum


class KeyCode(IntEnum):
    """Numpad key codes for Vintage Story."""

    NUM0 = 67
    NUM1 = 68
    NUM2 = 69
    NUM3 = 70
    NUM4 = 71
    NUM5 = 72
    NUM6 = 73
    NUM7 = 74
    NUM8 = 75
    NUM9 = 76
    DIV = 77
    MULT = 78
    SUB = 79
    ADD = 80
    DEC = 81


class Icon(StrEnum):
    """Available waypoint icons in Vintage Story."""

    CIRCLE = "circle"
    PLAYER = "player"
    TURNIP = "turnip"
    GRAIN = "grain"
    APPLE = "apple"
    BERRIES = "berries"
    MUSHROOM = "mushroom"
    BEE = "bee"
    CAVE = "cave"
    GEAR = "gear"
    GRAVESTONE = "gravestone"
    HOME = "home"
    LADDER = "ladder"
    PICK = "pick"
    PROPICK = "propick"
    ROCKS = "rocks"
    RUINS = "ruins"
    SKULL_AND_CROSSBONES = "skull_and_crossbones"
    SPIRAL = "spiral"
    STAR1 = "star1"
    STAR2 = "star2"
    TRADER = "trader"
    TREE = "tree"
    TREE2 = "tree2"
    VESSEL = "vessel"
    X = "x"
    CROSS = "cross"


@dataclass
class Category:
    """A waypoint category with default styling."""

    name: str
    key_code: KeyCode
    default_icon: Icon
    default_color: str


@dataclass
class Waypoint:
    """A single waypoint definition."""

    category: Category
    name: str
    key_code: KeyCode
    color: str | None = None
    icon: Icon | None = None

    # Resolved values (populated in __post_init__)
    resolved_color: str = field(init=False)
    resolved_icon: Icon = field(init=False)

    def __post_init__(self) -> None:
        """Set resolved values from category defaults."""
        self.resolved_color = self.color or self.category.default_color
        self.resolved_icon = self.icon or self.category.default_icon


# Map keycodes to numpad key display names
KEYCODE_TO_NAME: dict[KeyCode, str] = {
    KeyCode.NUM0: "0",
    KeyCode.NUM1: "1",
    KeyCode.NUM2: "2",
    KeyCode.NUM3: "3",
    KeyCode.NUM4: "4",
    KeyCode.NUM5: "5",
    KeyCode.NUM6: "6",
    KeyCode.NUM7: "7",
    KeyCode.NUM8: "8",
    KeyCode.NUM9: "9",
    KeyCode.DIV: "/",
    KeyCode.MULT: "*",
    KeyCode.SUB: "-",
    KeyCode.ADD: "+",
    KeyCode.DEC: ".",
}
