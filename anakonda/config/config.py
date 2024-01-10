from os import environ


class Config:
    ENV = environ.get("ANAKONDA_API_ENV", "production")
    DEBUG = bool(int(environ.get("ANAKONDA_API_DEBUG", "0")))
    TESTING = DEBUG
    SECRET_KEY = environ.get("ANAKONDA_API_SECRET_KEY", "secretkey")
    SQLALCHEMY_DATABASE_URI = environ.get("ANAKONDA_API_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    TIMEZONE = environ.get("ANAKONDA_API_TIMEZONE", "Asia/Tehran")
