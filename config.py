import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'change-me'


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