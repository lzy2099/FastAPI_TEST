# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    decription: str = Field(None, title="The descrptiong's description.", max_length=100)
    price: float = Field(None, gt=0, description="The price must be greater than 0.", title="greater than 0")
    tax: float = None


@app.put("/items/{item_id}/")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    result = {"item_id": item_id, "item": item}
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port="8000")
