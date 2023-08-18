from typing import cast
from dimensions import Dimension

import msgs


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
