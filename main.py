from classes import Box, Product

from schemas import Request, Response

import uvicorn

from fastapi import FastAPI


app = FastAPI()


@app.post('/')
def calculate(request: Request) -> Response:
    product = Product.from_request(request)
    box = Box.from_request(request, product)
    return box.get_packing()


if __name__ == '__main__':
    uvicorn.run(app)
