import spotipy
import spotipy.util as util
import os
import sys

scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'
token1 = util.prompt_for_user_token(sys.argv[1], scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')

print(token1)