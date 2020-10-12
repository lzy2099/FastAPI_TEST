# -*- coding: UTF-8 -*-
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.post("/files/")
async def files(
    request: Request,
    files_list: List[bytes] = File(...),
    files_name: List[UploadFile] = File(...),
    ):
    return templates.TemplateResponse("file.html",{
    "request": request,
    "file_sizes": [len(file) for file in files_list],
    "filenames": [file.filename for file in files_name],
    })

@app.post("/create_file/")
async def create_file(
    request: Request,
    file: bytes = File(...),
    fileb: UploadFile = File(...),
    notes: str = Form(...),
):
    return templates.TemplateResponse("file.html",
    {
    "request": request,
    "file_name": fileb.filename,
    "file_size": len(file),
    "notes": notes,
    "fileb_content_type": fileb.content_type,
    }
    )

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("post_files.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
