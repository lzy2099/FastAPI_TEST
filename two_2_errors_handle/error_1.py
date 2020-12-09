# -*- coding:utf-8 -*-
from fastapi import FastAPI, HTTPException

app = FastAPI()
items = {
    "foo": "The Foo Item",
    "bar": "The Bar Item",
}


@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found!")
    pass
    return {"Item": items[item_id]}


# 添加自定义标题
@app.get("/items-header/item_id")
async def item_id_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found.",
            headers={"X-error": "There goes error."}
        )
    return {"Item": items[item_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port="8000")
