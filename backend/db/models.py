from sqlalchemy import Column, DateTime, Integer, func

from backend.app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
