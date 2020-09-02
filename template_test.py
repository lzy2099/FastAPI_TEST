# -*- coding: UTF-8 -*-
from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello':'Hi~~'})

@app.get("/{say}/")
async def get_say(request: Request, say):
    return templates.TemplateResponse('index.html', {'request': request, 'say': say})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
