import os

class Config:
    # Load database URL from environment variable
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Secret key for session management
    SECRET_KEY = os.getenv('SECRET_KEY')  
