# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/item/")
async def get_item(ads_id: str = Cookie(None), ads_id2: int = Cookie(None)):
    return {"ads_id": ads_id, "ads_id2": ads_id2}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port="8000")
