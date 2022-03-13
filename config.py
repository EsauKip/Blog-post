import os
import re

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='1a6c4143b228d08b6025c2e4b543c627'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:kiprono12@localhost/blogpost'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
