from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String

from database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(255))
    email = Column(String(50))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
