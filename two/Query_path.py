# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/{item_id}/")
async def items(  # 验证item_id必填，长度大于等于10 小于等于20 如果类型是str 则ge le 不可用，否则报错
        item_id: int = Path(..., title="The ID of the item", ge=10, le=20),
        q: str = Query(None, alias="item_query"),
        size: float = Query(1, gt=0, lt=10.0)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
