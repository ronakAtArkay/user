from typing import List

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr


class UserShow(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserList(BaseModel):
    count: int
    list: List[UserShow]

    class Config:
        orm_mode = True
