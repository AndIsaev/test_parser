from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from backend.config import API_URL, SWAGGER_URL

db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    app = Flask('articles')

    app.config['SECRET_KEY'] = '123'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:super@db/backend'

    with app.app_context():
        # app.config.from_object(cfg.flask)

        db.init_app(app)
        migrate.init_app(app, db)

        spec = APISpec(
            title='backend REST API',
            version='1.0.',
            openapi_version='3.0.0',
            plugins=[FlaskPlugin(), MarshmallowPlugin()],
            info=dict(description='This is the swagger file that goes with our server code'),
            servers=[{'url': '/'}],
        )

        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={'app_name': 'backend'},
        )
        from backend.apps.articles.routes import articles_api

        app.register_blueprint(swaggerui_blueprint)
        app.register_blueprint(articles_api)

        for rule in app.url_map.iter_rules():
            func = app.view_functions[rule.endpoint]
            spec.path(view=func)

    @app.route('/swagger_spec')
    def get_apispec() -> dict:
        return spec.to_dict()

    return app
