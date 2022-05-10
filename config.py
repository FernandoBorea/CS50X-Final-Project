class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevConfig(Config):
    ENV = 'development'

class ProdConfig(Config):
    ENV = 'production'