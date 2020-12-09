# -*- coding:utf-8 -*-
from starlette.exceptions import HTTPException as StarletteHttpResponse
from starlette.responses import PlainTextResponse
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError


app = FastAPI()


# 覆盖默认异常处理程序
@app.exception_handler(StarletteHttpResponse)
async def unicorn_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handle(request, exc):
    return PlainTextResponse(str(exc),status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope, i dont think 3.")
    return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port="8000")
