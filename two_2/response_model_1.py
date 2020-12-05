from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
