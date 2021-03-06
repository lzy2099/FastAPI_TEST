# -*- coding:utf-8 -*-
from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.post("/create_file/")
async def create_file(file: bytes = File(...), fileb: UploadFile = File(...)):
    return {"file_size": len(file),
            "fileb_contant_type": fileb.content_type}


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("file_post.html", {'request': request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
