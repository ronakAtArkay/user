from fastapi import FastAPI

import models
from database import engine
from routers.admin.v1 import api as Admin_v1

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="user")

app.include_router(Admin_v1.router)
