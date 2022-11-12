from sqlalchemy import Column, DateTime, func, Integer

from backend.app import db


class BaseModel(db.Model):  # type: ignore
    __abstract__ = True

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
