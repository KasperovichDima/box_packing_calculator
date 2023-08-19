from pydantic import BaseModel, computed_field
from pydantic.dataclasses import dataclass

from exceptions import OversizeError

import project_typing as t

from msgs import MsgGenerator


@dataclass
class Request:
    """Income request scheme."""

    lng: t.Language
    box_sizes: tuple[float, float, float]
    product_sizes: tuple[float, float, float]

    def __post_init__(self):
        """Parameters validation."""
        def check_oversize():
            for s in self.product_sizes:
                if s > max(self.box_sizes):
                    raise OversizeError(self.product_sizes)

        check_oversize()


class Response(BaseModel):
    """Response scheme."""

    lng: t.Language
    optymal_position: t.Position
    product_lwh: tuple[float, float, float]
    pcs_in_row: int
    rows_in_layer: int
    layesr_in_box: int

    @computed_field  # type: ignore[misc]
    @property
    def total_amount(self) -> int:
        return self.pcs_in_row * self.rows_in_layer * self.layesr_in_box

    @computed_field  # type: ignore[misc]
    @property
    def response_msg(self) -> str:
        return MsgGenerator(self).get_response_msg()
