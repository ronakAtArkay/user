from typing import List

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from dependencies import get_db
from routers.admin.v1.crud import user
from routers.admin.v1.schemas import UserBase, UserList, UserShow

router = APIRouter()

# start user

# create api
@router.post("/user", tags=["user"])
def add_user(user_schema: UserBase, db: Session = Depends(get_db)):
    data = user.add_user(user_schema=user_schema, db=db)
    return data


# get_user_by_id api
@router.get("/user/{user_id}", response_model=UserShow, tags=["user"])
def get_user(
    user_id: str = Path(min_length=36, max_length=36), db: Session = Depends(get_db)
):
    data = user.get_user(user_id=user_id, db=db)
    return data


# get_user_list api
@router.get("/user", response_model=UserList, tags=["user"])
def get_user_list(
    start: int = 0,
    limit: int = 10,
    sort_by: str = Query("all", min_length=3, max_length=50),
    order: str = Query("all", min_length=3, max_length=4),
    search: str = Query("all", min_length=3, max_length=50),
    db: Session = Depends(get_db),
):
    data = user.get_user_list(
        start=start, limit=limit, sort_by=sort_by, order=order, search=search, db=db
    )
    return data


# get_all_user api
@router.get("/user/all/", response_model=List[UserShow], tags=["user"])
def get_all_user(db: Session = Depends(get_db)):
    data = user.get_all_users(db=db)
    return data


# update user api
@router.put("/user/{user_id}", response_model=UserShow, tags=["user"])
def update_user(
    user_schema: UserBase,
    user_id: str = Path(min_length=36, max_length=36),
    db: Session = Depends(get_db),
):
    data = user.update_user(user_schema=user_schema, user_id=user_id, db=db)
    return data


# delete user api
@router.delete("/user/{user_id}", tags=["user"])
def deleted_user(
    user_id: str = Path(min_length=36, max_length=36), db: Session = Depends(get_db)
):
    data = user.delete_user(user_id=user_id, db=db)
    return data


# end user
