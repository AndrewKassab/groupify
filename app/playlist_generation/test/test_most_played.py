#Added
#####################
import sys
sys.path.append('../')
#####################

from p_factory import PlaylistFactory
from user import User
from track import Track
import spotipy
import spotipy.util as util
import os

#Added
import createplaylist

username1 = "" 
username2 = "123881475"

token1 = ''
token2 = ''

scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'
token1 = util.prompt_for_user_token(username1, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')
token2 = util.prompt_for_user_token(username2, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')

users = {}
users[username1] = None
users[username2] = None
test = createplaylist
test.create_playlist([username1,username2],[token1,token2],users, 3600000)
