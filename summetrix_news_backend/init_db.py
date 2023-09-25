from extensions import db
from app import app

# Import your models
from models.news import News
with app.app_context():

    # Create the database tables
    db.create_all()