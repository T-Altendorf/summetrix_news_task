from flask import Flask
from flask_cors import CORS
from extensions import db, ma

def register_extensions(app):
    db.init_app(app) 
    ma.init_app(app)

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsapp.db'

    register_extensions(app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    # load the config
    app.config.from_pyfile('config.py', silent=True)
    from api.news import news_api
    app.register_blueprint(news_api, url_prefix='/api')  # Register the blueprint under '/api'

    return app
# Import and register API blueprints

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)