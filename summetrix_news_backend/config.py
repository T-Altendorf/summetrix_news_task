import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="summetrix_news_backend/.env")


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///newsapp.db"
    )
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    CORS_RESOURCES = os.environ.get("CORS_RESOURCES", {r"/*": {"origins": "*"}})
    DEBUG = os.environ.get("DEBUG", False)
    # You can add more configurations as needed


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


# More configurations like TestingConfig can be added as needed
