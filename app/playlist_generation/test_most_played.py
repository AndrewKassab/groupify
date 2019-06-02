#Added
#####################
import sys
sys.path.append('../')
#####################

from src.user import User
from src.track import Track
from src.p_factory import PlaylistFactory
import spotipy
import spotipy.util as util
import os

#Added
from src import createplaylist

username1 = "123881475"
username2 = "12185001442" 

token1 = 'BQDeYIv9NJxSJTmY2R_y8BJuFMy5LBlaSqyxAAQGbw7E7KDbXhE--_QTW41XMUIj-CigfRhAsVPZpZKPNKyeZrkCvqMHZHpm56mCj3aNyuvHhZWZHJtE8mS38kvr6VrkDBHDbrx-N-jbRocj9h5KLs3Rosxns_gTMNzZeEIrOu1HhBlyRN0PPi2yNJnSz2hHP-HdPQd9N6SLZXPZ8zwOIuhZz32ofpfA0HHY0U5Qq8RI5yyLERV1QA'
token2 = 'BQDFVqHYoDacdS9pRDgVNlD0ecPVgwkyofTnplGEB5byqiWjtIhIpc4CLfhmTy92-fCe8YLb9bjpPY0BpDGWuEpbvQv71BXbENKfydTd3B27zgw82yagWm6BgKE_kP8ECB3YM8-8OuqhCjc75cEfpLUwcXuYR8_aGl60XDyLrieBD-0jTumWdOckAQlEJB1YO4X6XxPlNEbe8wlntMjrGZmp8fVcB2cCpAS7o59zNqwm2SVklr33GPWW'

scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'

users = {}
users[username1] = None
users[username2] = None
test = createplaylist
test.create_playlist([username1,username2],[token1,token2],users, 3600000)
