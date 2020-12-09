# -*- coding:utf-8 -*-
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import FastAPI, HTTPException


# 自定义异常处理程序 UnicornException,继承自Exception 基类
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oopfs! {exc.name} did someting. There goes a rainbow..."
        },
    )


@app.get("/unicorns/{name}")
async def read_unicorns(name: str):
    if name == "yoyo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port="8000")
