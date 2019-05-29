import os

# Configuration object spscifically for setting up the database
class Config(object):
    user = os.environ['DB_USER']
    password = os.environ['DB_PASS']
    host = os.environ['DB_HOST']
    port = os.environ['DB_PORT']
    database = f'groupify_{os.environ["FLASK_ENV"]}'

    SQLALCHEMY_DATABASE_URI = f'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

ERR_401 = 'No such user found'
ERR_404 = 'Playlist not found'

SPOTIFY_
