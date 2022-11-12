import datetime

from flask import Blueprint, Response, make_response

from backend.apps.articles import Article
from backend.config import BASE_ROUTE
from backend.db.db import DbSession

articles_api = Blueprint('article_route', __name__, url_prefix=f'{BASE_ROUTE}/article')


@articles_api.route('/', methods=['GET'])
def get_information():
    now = datetime.datetime.now().date()

    with DbSession(read_only=True) as db_session:
        themes = db_session.query(Article).filter_by(date_of_published=now)
        return make_response({'data': [theme_schema.dump(theme) for theme in themes]}, 200)
