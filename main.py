from fastapi import FastAPI
from routers.admin.v1 import api as Admin_v1
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="user")

app.include_router(Admin_v1.router)