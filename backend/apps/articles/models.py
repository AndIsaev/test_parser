from sqlalchemy import Column, Date, Text

from backend.db import BaseModel


class Article(BaseModel):
    __tablename__ = 'article'

    title = Column(Text)
    url_img = Column(Text)
    date_of_published = Column(Date)
