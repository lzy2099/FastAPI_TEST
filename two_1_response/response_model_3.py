from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 0.5
    tags: List[str] = []


items = {
    "foo": {"name": "foo", "price": 50.1},
    "bar": {"name": "bar", "description": "The bartenders", "price": 66, "tax": 1.1},
    "bz": {"name": "bz", "description": None, "price": 99, "tax": 2.1, "tags": []},
}


# response_model_exclude_unset 仅返回已列出items中包含的值，没有的不返回。
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# response_model_exclude 不包含，剔除某项值。
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
