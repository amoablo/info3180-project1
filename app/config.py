import os

class Config(object):
    """Base Config Object"""
    """ Extra comment"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') or 'postgres://jitgzcbregaumx:844e1486da1b558d228a131d531d09a8dcbb12b9b2b4a4c77a53f32fe50cc208@ec2-54-167-168-52.compute-1.amazonaws.com:5432/d9dv6mpn2fnvc4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or './uploads'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object  """
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False