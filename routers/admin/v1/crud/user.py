from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from libs.utils import generate_id, now
from models import UserModel
from routers.admin.v1.schemas import UserBase


# create user
def add_user(user_schema: UserBase, db: Session):
    id = generate_id
    db_user = UserModel(id=id(), name=user_schema.name, email=user_schema.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# get_user_by_id function
def get_user_by_id(user_id: str, db: Session):
    return (
        db.query(UserModel)
        .filter(UserModel.id == user_id, UserModel.is_deleted == False)
        .first()
    )


# use get_user_by_id function
def get_user(user_id: str, db: Session):
    db_user = get_user_by_id(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user is Not Found"
        )
    return db_user


# show user by list
def get_user_list(
    start: int, limit: int, sort_by: str, order: str, search: str, db: Session
):
    query = db.query(UserModel).filter(UserModel.is_deleted == False)
    if search != "all":
        text = f"""%{search}%"""
        query = query.filter(or_(UserModel.name.like(text)))

    if sort_by == "name":
        if order == "desc":
            query = query.order_by(UserModel.name.desc())
        else:
            query = query.order_by(UserModel.name)

    else:
        query = query.order_by(UserModel.updated_at.desc())

    results = query.offset(start).limit(limit).all()
    count = query.count()
    data = {"count": count, "list": results}
    return data


# show all users
def get_all_users(db: Session):
    db_user = (
        db.query(UserModel)
        .filter(UserModel.is_deleted == False)
        .order_by(UserModel.name.desc())
        .all()
    )
    return db_user


# update a user
def update_user(user_schema: UserBase, user_id: str, db: Session):
    db_user = get_user_by_id(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user is Not Found"
        )
    db_user.name = user_schema.name
    db_user.email = user_schema.email
    db_user.updated_at = now()
    db.commit()
    db.refresh(db_user)
    return db_user


# delete a user
def delete_user(user_id: str, db: Session):
    db_user = get_user_by_id(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user is Not Found"
        )
    db_user.is_deleted = True
    db.commit()
    db.refresh(db_user)
    return f"{db_user.name} is deleted successfully"
