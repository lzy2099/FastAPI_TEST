# -*- coding:UTF-8 -*-
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.post("/files")
async def files(
        request: Request,
        files_list: List[bytes] = File(...),
        files_name: List[UploadFile] = File(...),
):
    return templates.TemplateResponse("index_file.html",
                                      {
                                          "request": Request,
                                          "file_size": [len(files) for file in files_list],
                                          "file_name": [file.filename for file in files_name],
                                      })