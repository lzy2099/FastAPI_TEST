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
    "bz": {"name": "BZ", "description": None, "price": 40.8, "tax": 31, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]      # item 数据
    stored_item_model = Item(**stored_item_data)     # item 模型
    update_data = item.dict(exclude_unset=True)
    print('update_data', update_data)
    updated_item = stored_item_model.copy(update=update_data)
    print('updated_item', jsonable_encoder(updated_item))
    items[item_id] = jsonable_encoder(updated_item)
    print("items[item_id", items[item_id])
    return updated_item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
