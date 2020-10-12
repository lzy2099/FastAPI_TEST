# -*- coding:UTF-8 -*-
from fastapi import FastAPI, Form
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.post("/user/")
async def files(
    request: Request,
    username:str = Form(...),
    password:str = Form(...),
    ):
    print("username", username)
    print("password", password)
    return remplates.TemplateResponse(
    'boostrap_index.html',
    {
        'request': request,
        'username': username,

    } )

@app.get("/")
async def main(request: Request)
    return templates.TemplateResponse('signin.html', {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
