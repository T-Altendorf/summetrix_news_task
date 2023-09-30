from flask import Flask
from flask_cors import CORS
from extensions import db, ma

from config import Config


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)


def create_app(config_class=Config):
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    CORS(app, resources=app.config["CORS_RESOURCES"])

    # Register the blueprint under '/api'
    from api.news import news_api

    app.register_blueprint(news_api, url_prefix="/api")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
