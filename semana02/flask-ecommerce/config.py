import os
from dotenv import load_dotenv
import datetime

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    # JWT_ACCESS_TOKEN_EXPIRES = 3600 # En segundos
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)