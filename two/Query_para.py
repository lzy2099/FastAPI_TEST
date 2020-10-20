# -*- coding: UTF-8 -*-
from fastapi import FastAPI

app = FastAPI()
items = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name": "QZ"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip:skip+limit]


@app.get("/i/")
async def read_i(a: str = "Hello, ", b: str = "the ", c: str = "world."):
    return {"ABC": a+b+c}, {"AC": a+c}


@app.get("/ii/")
async def read_ii(a: int = 1, b: int = 10, c: int = 20):
    return {"ABC": a+b+c}, {"BC": b+c}


@app.get("/iii/")
async def read_iii(a: int = 5, b: int = 10, c: int=15):
    return "a+b+c", a+b+c


@app.get("/oh/{item_id}")
async def oh(item_id: str, name: str = None, happy: bool = False):
    item = {"item_id": item_id}
    if name:
        item.update({"name": name})
    if not happy:
        item.update({"item_id": "I'm not Happy."})
    return item
# http://127.0.0.1:8000/oh/TV?name=John&happy=True


@app.get("/user/{user_id}/item/{item_id}/")
async def duo_para(
        user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This a long item with a long description"})
    return item
# 比较两个链接结果的差别
# http://127.0.0.1:8000/user/23/item/BBC/
# http://127.0.0.1:8000/user/23/item/BBC/?q=bango&short=True


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
