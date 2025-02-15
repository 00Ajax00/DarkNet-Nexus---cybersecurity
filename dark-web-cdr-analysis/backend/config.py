import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
    REDIS_URL = os.getenv("REDIS_URL")
    JWT_SECRET = os.getenv("JWT_SECRET")
