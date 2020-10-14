# -*- coding: UTF-8 -*-
from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post.html', {'request':request})


@app.post("/user/")
async def get_userpass(request: Request, username: str=Form(...), password: str=Form(...)):
    return templates.TemplateResponse('index.html', {'request':request, 'username':username, 'password': password})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
