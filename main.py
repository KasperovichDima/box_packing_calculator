from dataclasses import dataclass
from enum import Enum
from operator import mul
from typing import (
    Iterator,
    NewType,
    cast,
)
from functools import reduce

import msgs


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


pos_translate: dict[Position, str] = {
    Position.EDGE_ACROSS: 'Боком поперек коробки',
    Position.EDGE_ALONG: 'Боком вдоль коробки',
    Position.FLAT_ACROS: 'Плашмя поперек коробки',
    Position.FLAT_ALONG: 'Плашмя вдоль коробки',
    Position.UP_ACROSS: 'Стоя поперек коробки',
    Position.UP_ALONG: 'Стоя вдоль коробки',
}


def get_dimensions(msg: str) -> Dimension | None:
    """Get correct dimesnions from user or None if just Enter pressed."""

    def dimensions_are_valid() -> bool:
        """Check all dimensions are positive and len is correct."""
        nums_gt_zero = True
        for dim in dimensions:
            if dim <= 0:
                nums_gt_zero = False
        if not nums_gt_zero:
            print(msgs.NEG_DIMENSIONS)
        if len(dimensions) != 3:
            print(msgs.WRONG_ARGS_NUM)
        return nums_gt_zero and len(dimensions) == 3

    done = False
    while not done:
        user_input = input(msg)
        if not user_input:
            return None
        try:
            dimensions = cast(
                Dimension,
                tuple(float(side) for side in user_input.split())
            )
            if dimensions_are_valid():
                done = True
        except ValueError:
            print(msgs.WRONG_ARGS)

    return dimensions


@dataclass
class Cuboid:

    length: float
    width: float
    heigth: float

    @classmethod
    def create(cls, msg: str):
        while not (dimensions := get_dimensions(msg)):
            print(msgs.WRONG_ARGS_NUM)
        return cls(*dimensions)

    def resize(self, msg: str) -> None:
        if not (dimensions := get_dimensions(msg)):
            return
        self.length, self.width, self.heigth = dimensions


@dataclass
class Product(Cuboid):

    def get_dimensions(self, position: Position) -> Iterator[float]:
        '''Get product dimensions in one of 6 positions.'''
        return (self._sorted_dimensions[ind] for ind in position.value)  # type: ignore  # noqa: E501

    @property
    def _sorted_dimensions(self) -> list[float]:
        return sorted([self.length, self.width, self.heigth])


@dataclass
class Box(Cuboid):

    pcs_in_line = 0
    lines_in_layer = 0
    layers_in_box = 0
    total_box_pcs = 0
    optymal_position = Position.EDGE_ACROSS

    def __post_init__(self):
        self.product = Product.create(msgs.PROD)

    def get_packing(self) -> None:

        def get_position_packing() -> tuple[int, int, int]:

            prod_dimensions = (self.product.get_dimensions(pos))

            lines_in_layer = int(self.length // next(prod_dimensions))
            pcs_in_line = int(self.width // next(prod_dimensions))
            layers_in_box = int(self.heigth // next(prod_dimensions))

            return pcs_in_line, lines_in_layer, layers_in_box

        self.total_box_pcs = 0

        def get_total_amount():
            return reduce(mul, get_position_packing())

        def set_new_packing():
            self.pcs_in_line, self.lines_in_layer, self.layers_in_box\
                = get_position_packing()
            self.optymal_position = pos
            self.total_box_pcs = get_total_amount()

        for pos in Position:
            if get_total_amount() > self.total_box_pcs:
                set_new_packing()

        print(msgs.RESULT.format(pos=pos_translate[self.optymal_position],
                                 in_line=self.pcs_in_line,
                                 lines=self.lines_in_layer,
                                 layers=self.layers_in_box,
                                 pcs=self.total_box_pcs))


def main():
    print('Welcome to box calculator 0.1')
    box = Box.create(msgs.BOX)
    box.get_packing()
    while True:
        box.resize(msgs.SAME_BOX)
        box.product.resize(msgs.SAME_PROD)
        box.get_packing()


if __name__ == '__main__':
    main()
