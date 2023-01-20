from pydantic import BaseModel, Field, EmailStr
from typing import List


class UserBase(BaseModel):
    name : str = Field(min_length = 2, max_length = 50)
    email : EmailStr 


class UserShow(BaseModel):
    name : str
    email : str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    count : int
    list : List[UserShow]

    class Config:
        orm_mode = True