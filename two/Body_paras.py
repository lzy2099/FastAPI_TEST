# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# 混合参数
@app.put("/items/{item_id}/")
async def update_items(
        item_id: int = Path(..., title="The ID of item.", ge=0, le=10),
        q: str = None,
        item: Item = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
