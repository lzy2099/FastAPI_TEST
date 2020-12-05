# -*- coding:utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.4


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 67, "tax": 20.4},
    "bz": {"name": "Bz", "description": "Goes by Bz", "price": 88, "tax": 34},
}


# response_model_include 返回列出的值，没有列出的不返回。
@app.get("/items/{item_id}/name", response_model=Item, response_model_include=["name", "description", "tax"])
async def read_item(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)