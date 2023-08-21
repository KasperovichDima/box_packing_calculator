from typing import Annotated

from classes import (
    Box,
    Product,
)

from examples import request

from fastapi import (
    Body,
    FastAPI,
)

from schemas import (
    Request,
    Response,
)

import uvicorn


app = FastAPI()


@app.post('/calculate', response_model=Response)
def calculate(request: Annotated[Request, Body(examples=request)]):
    product = Product.from_request(request)
    box = Box.from_request(request, product)
    return box.get_packing()


if __name__ == '__main__':
    uvicorn.run(app)
