from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    passwd: str
    email: EmailStr
    fullname: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    fullname: str = None


@app.post("/user/", response_model=UserOut)
async def create_item(*, user: UserIn):
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
