from examples import response

from exceptions import OversizeError

from msgs import MsgGenerator

import project_typing as t

from pydantic import (
    BaseModel,
    Field,
    computed_field
)
from pydantic.dataclasses import dataclass


@dataclass
class Request:
    """Income request scheme."""

    lng: t.Language = Field(description='2 letters available language code')
    box_sizes: t.Dimensions = Field(description='Box dimensions')
    product_sizes: t.Dimensions = Field(description='Product dimensions')

    def __post_init__(self):
        """Parameters validation."""
        def check_oversize():
            for s in self.product_sizes:
                if s > max(self.box_sizes):
                    raise OversizeError(self.product_sizes)

        check_oversize()


class Response(BaseModel):
    """Response scheme."""

    lng: t.Language = Field(exclude=True)
    optymal_position: str
    product_lwh: tuple[float, float, float]
    pcs_in_row: int
    rows_in_layer: int
    layesr_in_box: int
    total_amount: int

    model_config = {
        "json_schema_extra": {
            "examples": [response]
        }
    }

    @computed_field  # type: ignore[misc]
    @property
    def response_msg(self) -> str:
        return MsgGenerator(self).get_response_msg()
