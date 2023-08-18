from enum import Enum
from typing import NewType


DimensionIndexes = NewType('DimensionIndexes', tuple[float, float, float])
Dimension = tuple[float, float, float]


class Position(Enum):
    """6 product positions in the box."""
    EDGE_ACROSS = DimensionIndexes((0, 2, 1))
    EDGE_ALONG = DimensionIndexes((2, 0, 1))
    FLAT_ACROS = DimensionIndexes((1, 2, 0))
    FLAT_ALONG = DimensionIndexes((2, 1, 0))
    UP_ACROSS = DimensionIndexes((0, 1, 2))
    UP_ALONG = DimensionIndexes((1, 0, 2))
