import os

class Config:
   '''
   General configuration parent class
   '''
   pass
   # simple mde  configurations
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/ktown003'
   MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
   MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   UPLOADED_PHOTOS_DEST = "app/static/photos"
   SUBJECT_PREFIX = 'K-movies'
   MAIL_USERNAME="developersjuniors@gmail.com"
   MAIL_PASSWORD="Nairobi001"
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_TRACK_MODIFICATIONS=False

# simple mde  configurations
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True
   @staticmethod
   def init_app(app):
        pass

class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/movies-test'
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/ktown003'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
