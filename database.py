from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = (
    "mysql+mysqlconnector://root:%s@localhost:3306/crud" % quote("Arkay@210")
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)

Base = declarative_base()