import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{un}:{pw}@db:5432/{db}'.format(
        un=os.environ['DB_USERNAME'],
        pw=os.environ['DB_PASSWORD'],
        db=os.environ['DB_DATABASE']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_DEBUG = True


class TestingConfig(Config):
    TESTING = True
