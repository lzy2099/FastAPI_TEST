# -*- coding:utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = None
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 90},
    "bar": {"name": "Bar", "description": "The Bar Item.", "price": 20, "tax": 19},
    "bz": {"name": "BZ", "description": None, "price": 40, "tax": 3, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    print(items)
    return update_item_encoded


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
