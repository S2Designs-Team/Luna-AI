from enum import Enum, Flag, auto

class EnumLayout(Enum):
    NONE       = 0
    VERTICAL   = 1
    HORIZONTAL = 2
    FLOW       = 3


class EnumSides(Flag):
    UP_SIDE     = auto()
    RIGHT_SIDE  = auto()
    BOTTOM_SIDE = auto()
    LEFT_SIDE   = auto()
    ALL_SIDES   = UP_SIDE | RIGHT_SIDE | BOTTOM_SIDE | LEFT_SIDE

class EnumCorners(Flag):
    TOP_LEFT     = auto()
    TOP_RIGHT    = auto()
    BOTTOM_LEFT  = auto()
    BOTTOM_RIGHT = auto()
    TOP_SIDE     = auto()
    RIGHT_SIDE   = auto()
    BOTTOM_SIDE  = auto()
    LEFT_SIDE    = auto()
    ALL_CORNERS  = TOP_LEFT | TOP_RIGHT | BOTTOM_LEFT | BOTTOM_RIGHT