from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "hello world!"}

@app.get("/names/{name}/")
def read_name(name: str):
    return {"name is": name}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
