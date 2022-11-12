import datetime

from flask import Blueprint, make_response
from sqlalchemy import and_

from backend.apps.articles import Article
from backend.apps.articles.schema import article_schema
from backend.config import BASE_ROUTE
from backend.db.db import DbSession

articles_api = Blueprint('article_route', __name__, url_prefix=f'{BASE_ROUTE}/article')


@articles_api.route('/', methods=['GET'])
def get_information():
    now = datetime.datetime.now().date()
    four_days = datetime.timedelta(days=4)

    with DbSession(read_only=True) as db_session:
        articles = (
            db_session.query(Article).where(
                and_(
                    Article.date_of_published == now,
                    Article.date_of_published >= now - four_days,
                ),
            )
        ).order_by(Article.id.desc())
        return make_response({'data': [article_schema.dump(article) for article in articles]}, 200)
