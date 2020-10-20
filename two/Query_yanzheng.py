# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


# 限制长度
@app.get("/items_limit/")
async def gets_items(q: str = Query(None, min_length=2, max_length=10)):  # 如果将 None 改为 ... 则此项是必填项
    results = {"items": [{'item_id': "puppy"}, {"item_id": "kitty"}]}
    if q:
        results.update({"q": q})
    return results


# 正则匹配
@app.get("/items_regex/")
async def gets_tems2(q: str = Query(None, min_length=2, max_length=20, regex="^A")):  # 要求参数必须要字母A开头
    results = {"items": [{"item_id": "appale"}, {"item_id": "orange"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
