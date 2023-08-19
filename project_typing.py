from enum import Enum
from typing import NewType


_DimensionIndexes = NewType('_DimensionIndexes', tuple[float, float, float])
Dimensions = tuple[float, float, float]


class Position(Enum):
    """6 product positions in the box."""
    EDGE_ACROSS = _DimensionIndexes((0, 2, 1))
    EDGE_ALONG = _DimensionIndexes((2, 0, 1))
    FLAT_ACROS = _DimensionIndexes((1, 2, 0))
    FLAT_ALONG = _DimensionIndexes((2, 1, 0))
    UP_ACROSS = _DimensionIndexes((0, 1, 2))
    UP_ALONG = _DimensionIndexes((1, 0, 2))


class Language(Enum):
    """Supported languages."""

    en = 'en'
    ru = 'ru'
