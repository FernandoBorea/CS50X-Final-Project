from os import environ, path

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = environ.get('SECRET_KEY')

class DevConfig(Config):
    ENV = 'development'

class ProdConfig(Config):
    ENV = 'production'