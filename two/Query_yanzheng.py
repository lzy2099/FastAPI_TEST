# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


# 限制请求参数的长度
@app.get("/items_limit/")
async def gets_items(q: str = Query(None, min_length=2, max_length=10)):  # 如果将 None 改为 ... 则此项是必填项
    results = {"items": [{'item_id': "puppy"}, {"item_id": "kitty"}]}
    if q:
        results.update({"q": q})
    return results


# 正则匹配请求参数的格式
@app.get("/items_regex/")
async def gets_tems2(q: str = Query(None, min_length=2, max_length=20, regex="^A")):  # 要求参数必须要字母A开头
    results = {"items": [{"item_id": "appale"}, {"item_id": "orange"}]}
    if q:
        results.update({"q": q})
    return results


# 接收列表形式的参数
@app.get("/items_list/")
async def items_list(q: List[str] = Query(["one", "two"])):
    query_items = {"q": q}
    return query_items


# http://127.0.0.1:8000/items_list/?q=one&q=two&q=three

# 参数别名
@app.get("/items_alias/")
async def items_alias(q: str = Query(None, alias="item_query")):
    results = {"items": [{"item_id": "good"}, {"item_id": "bad"}]}
    if q:
        results.update({"q": q})
    return results


# http://127.0.0.1:8000/items_alias/?item_query=saf  //传递参数需要使用item_query不能使用q ，使用q 将导致传递失败

# 弃用参数  打弃用标记，函数可以正常使用。提醒作用。
@app.get("/items_deprecate/")
async def items_alias(q: str = Query(
    None,
    alias="item_query",
    title="qi_yong",
    deprecated=True, )
):
    results = {"items": [{"item_id": "good"}, {"item_id": "bad"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
