from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from backend.apps.articles import Article
from backend.db.db import DbSession
from backend.db.schema import BaseSchemaMixin

db_session = DbSession()


class ArticleSchema(BaseSchemaMixin, SQLAlchemyAutoSchema):

    class Meta:
        model = Article
        load_instance = True
        sqla_session = db_session


article_schema = ArticleSchema()
