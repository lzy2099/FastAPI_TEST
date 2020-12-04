# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# 嵌入
@app.put("/items/{item_id}/")
async def update_items(
        item_id: int, item: Item = Body(..., embed=True)
):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
