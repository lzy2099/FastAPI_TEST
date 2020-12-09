# -*- coding:utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.encoders import jsonable_encoder

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    jsonable_comp_ietm_data = jsonable_encoder(item)
    fake_db[id] = jsonable_comp_ietm_data
    print(jsonable_comp_ietm_data)
    print(type(jsonable_comp_ietm_data))
    print(fake_db)
    print(type(fake_db))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
