"""Project exceptions."""
from fastapi import HTTPException


class OversizeError(HTTPException):
    """Raise if product is too large to be placed in the box."""

    def __init__(self, dimensions: list[float]) -> None:
        err_msg = f'Product with '\
                  f'length:{dimensions[0]} '\
                  f'width:{dimensions[1]} '\
                  f'heigth:{dimensions[2]} '\
                  f'can not be placed in the box.'
        super().__init__(status_code=400, detail=err_msg)
