class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/flask_api_app_dev'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/flask_api_app_test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/flask_api_app'