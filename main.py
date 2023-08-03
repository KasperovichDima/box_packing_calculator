# import tkinter
from dataclasses import dataclass
from enum import Enum
from typing import Iterator


class Position(Enum):
    """6 product positions in the box."""
    FLAT_ACROS = 1, 2, 0
    FLAT_ALONG = 2, 1, 0
    EDGE_ACROSS = 0, 2, 1
    EDGE_ALONG = 2, 0, 1
    UP_ACROSS = 0, 1, 2
    UP_ALONG = 1, 0, 2


@dataclass
class Cuboid:

    length: float
    width: float
    heigth: float


@dataclass
class Product(Cuboid):

    def get_dimensions(self, position: Position) -> Iterator[float]:
        '''Get product dimensions in one of 6 positions.'''
        return (self._sorted_dimensions[ind] for ind in position.value)

    @property
    def _sorted_dimensions(self) -> list[float]:
        return sorted([self.length, self.width, self.heigth])


@dataclass
class Box(Cuboid):

    product: Product

    def get_free_space(self, position: Position) -> float:

        def get_empty_volume():
            return sum((
                free_heigth * self.length * self.width,
                free_width * self.length * (self.heigth - free_heigth),
                free_length * (self.width - free_width)
                * (self.heigth - free_heigth)
            ))

        prod_dimensions = self.product.get_dimensions(position)

        # free_length = self.length % next(prod_dimensions)
        # free_width = self.width % next(prod_dimensions)
        # free_heigth = self.heigth % next(prod_dimensions)

        self._lines_in_layer, free_length = divmod(self.length,
                                                   next(prod_dimensions))
        self._pcs_in_line, free_width = divmod(self.width,
                                               next(prod_dimensions))
        self._layers_in_box, free_heigth = divmod(self.heigth,
                                                  next(prod_dimensions))

        return get_empty_volume()

    def get_packing(self, position: Position) -> None:
        pass


def get_box() -> Box:

    prod_msg = 'Input your product sizes\n'
    product_dimensions = sorted([float(side)
                                 for side in input(prod_msg).split()],
                                reverse=True)
    box_msg = 'Input your box sizes\n'
    l, w, h = sorted([float(side) for side in input(box_msg).split()],
                     reverse=True)
    product = Product(*product_dimensions)
    return Box(l, w, h, product)


def test_box():
    return Box(
        50, 10, 30,
        Product(7, 2, 4)
    )


print('Wellcome to box calculator 0.1')
box = test_box()
free_spaces = {box.get_free_space(pos): pos for pos in Position}
result = free_spaces[min(free_spaces)]
print(result)


def simple_function():
    print('I am a very simple function.')

