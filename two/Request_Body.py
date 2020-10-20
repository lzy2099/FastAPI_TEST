# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def creat_item(item: Item):
    print(item.dict())
    return item, '好好学习，天天向上。'


@app.put('/item/{item_id}/')
async def creat_items(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    print(result)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
