from datetime import datetime
from pydantic import BaseModel, EmailStr, conint

class UserCreate(BaseModel):
    email:  EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_atributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Vote(BaseModel):
    post_id: int
    direction: conint(ge=0, le=1)  # type: ignore
    class Config:
        from_atributes = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    user_id: int
    user: UserOut
    class Config:
        from_atributes = True



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str | None = None
