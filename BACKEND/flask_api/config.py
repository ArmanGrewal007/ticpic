import os

class Config:
    SECRET_KEY = os.urandom(24)
    SECURITY_PASSWORD_SALT = os.urandom(24)
    SECURITY_PASSWORD_HASH = 'argon2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False