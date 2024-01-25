import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "100"))
WEB_CONCURRENCY = int(os.getenv("WEB_CONCURRENCY", "2"))
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://"
    + config["db_user"]
    + ":"
    + config["db_pass"]
    + "@"
    + config["db_host"]
    + "/"
    + config["db_name"]
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=POOL_SIZE, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
