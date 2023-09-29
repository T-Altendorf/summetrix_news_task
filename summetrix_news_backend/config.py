import os
from dotenv import load_dotenv

#load_dotenv(dotenv_path='summetrix_news_backend/.env')
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///newsapp.db')    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') 
    CORS_RESOURCES = {r"/*": {"origins": "*"}}
    # You can add more configurations as needed

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# More configurations like TestingConfig can be added as needed