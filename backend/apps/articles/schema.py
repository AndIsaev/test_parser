from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from backend.db.schema import BaseSchemaMixin


class ArticleSchema(BaseSchemaMixin, SQLAlchemyAutoSchema):
    title = fields.String()
    description = fields.String()


article_schema = ArticleSchema()
