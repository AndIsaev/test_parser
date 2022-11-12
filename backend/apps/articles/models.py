from sqlalchemy import Column, Text, Date

from backend.db import BaseModel


class Article(BaseModel):
    __tablename__ = 'article'

    title = Column(Text)
    url_img = Column(Text)
    date_of_published = Column(Date)
    #
    # def __repr__(self) -> str:
    #     return f'Article: {self.title[:30]}'
    #
    # def __str__(self) -> str:
    #     return f'{self.name[:30]}'

