from dataclasses import dataclass
from operator import mul
from typing import Iterator, Self, cast
from functools import reduce

from project_typing import Dimensions, Language, Position

from schemas import Request, Response


pos_translate: dict[Position, str] = {
    Position.EDGE_ACROSS: 'Боком поперек коробки',
    Position.EDGE_ALONG: 'Боком вдоль коробки',
    Position.FLAT_ACROS: 'Плашмя поперек коробки',
    Position.FLAT_ALONG: 'Плашмя вдоль коробки',
    Position.UP_ACROSS: 'Стоя поперек коробки',
    Position.UP_ALONG: 'Стоя вдоль коробки',
}


@dataclass
class Cuboid:

    length: float
    width: float
    heigth: float


@dataclass
class Product(Cuboid):

    def get_pose_dimensions(self, position: Position) -> Iterator[float]:
        """Get product dimensions in specified positions."""
        return (self.lwh[ind] for ind in position.value)  # type: ignore  # noqa: E501

    @property
    def lwh(self) -> Dimensions:
        result = cast(
            Dimensions,
            tuple(sorted([self.length, self.width, self.heigth]))
        )
        return result

    @classmethod
    def from_request(cls, request: Request) -> Self:
        return cls(*request.product_sizes)


@dataclass
class Box(Cuboid):

    lng: Language
    product: Product
    pcs_in_row = 0
    rows_in_layer = 0
    layers_in_box = 0
    total_amount = 0
    optymal_position = Position.EDGE_ACROSS

    @classmethod
    def from_request(cls, request: Request, product: Product) -> Self:
        return cls(*request.box_sizes, request.lng, product)

    def get_packing(self) -> Response:

        def get_total_amount():
            return reduce(mul, get_packing())

        def get_packing() -> tuple[int, int, int]:

            prod_dimensions = (self.product.get_pose_dimensions(pos))

            lines_in_layer = int(self.length // next(prod_dimensions))
            pcs_in_line = int(self.width // next(prod_dimensions))
            layers_in_box = int(self.heigth // next(prod_dimensions))

            return pcs_in_line, lines_in_layer, layers_in_box

        def set_new_packing():
            self.pcs_in_row, self.rows_in_layer, self.layers_in_box\
                = get_packing()
            self.optymal_position = pos
            self.total_amount = get_total_amount()

        def get_response() -> Response:
            return Response(
                lng=self.lng,
                optymal_position=self.optymal_position,
                product_lwh=self.product.lwh,
                pcs_in_row=self.pcs_in_row,
                rows_in_layer=self.rows_in_layer,
                layesr_in_box=self.layers_in_box,
                )

        for pos in Position:
            if get_total_amount() > self.total_amount:
                set_new_packing()

        return get_response()
