# -*- coding: UTF-8 -*-

from fastapi import FastAPI
from enum import Enum


class Name(str, Enum):
    Jack = "杰克",
    Rose = "罗斯",
    Green = "格林",


app = FastAPI()


@app.get("/{who}")
async def get_day(who:Name):
    if who == Name.Jack:
        return {"who": who, "message":"杰克是捷克人"}
    if who.value == "罗斯":
        return {"who": who, "message":"罗斯是美国人"}
    return {"who": who, "message":"格林是德国人"}


@app.get("/")
async def main():
    return {"message": "你好，FastAPI"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
