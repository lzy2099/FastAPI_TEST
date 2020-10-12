# -*- coding: UTF-8 -*-

from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('temp_test.html', {'request': request, 'hello':'Hi~~'})


@app.get("/{words}/")
async def get_words(request:Request, words):
     return templates.TemplateResponse("temp_test.html", {"request": request, "hello": words})



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


