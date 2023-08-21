from dataclasses import dataclass
from functools import reduce
from operator import mul
from typing import (
    Iterator,
    Self,
    cast,
)

import project_typing as t

from schemas import Request, Response


@dataclass
class Cuboid:

    length: float
    width: float
    heigth: float


@dataclass
class Product(Cuboid):

    def get_pose_dimensions(self, position: t.Position) -> Iterator[float]:

        def get_sorted_lwh():
            return sorted([self.length, self.width, self.heigth])

        """Get product dimensions in specified positions."""
        return (get_sorted_lwh()[ind] for ind in position.value)  # type: ignore  # noqa: E501

    @classmethod
    def from_request(cls, request: Request) -> Self:
        return cls(*request.product_sizes)


@dataclass
class Box(Cuboid):

    lng: t.Language
    product: Product
    pcs_in_row = 0
    rows_in_layer = 0
    layers_in_box = 0
    total_amount = 0
    optymal_position = t.Position.EDGE_ACROSS

    @classmethod
    def from_request(cls, request: Request, product: Product) -> Self:
        return cls(*request.box_sizes, request.lng, product)

    @property
    def _product_lwh(self) -> t.Dimensions:
        result = cast(
            t.Dimensions,
            tuple(self.product.get_pose_dimensions(self.optymal_position))
        )
        return result

    def get_packing(self) -> Response:

        def get_total_amount():
            return reduce(mul, get_packing())

        def get_packing() -> tuple[int, int, int]:

            prod_dimensions = self.product.get_pose_dimensions(pos)

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
                optymal_position=self.optymal_position.name,
                product_lwh=self._product_lwh,
                pcs_in_row=self.pcs_in_row,
                rows_in_layer=self.rows_in_layer,
                layesr_in_box=self.layers_in_box,
                total_amount=self.total_amount,
                )

        for pos in t.Position:
            if get_total_amount() > self.total_amount:
                set_new_packing()

        return get_response()
