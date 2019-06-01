  
# Shows the top artists for a user
from createplaylist import create_playlist

import pprint
import sys

import spotipy
import spotipy.util as util
import simplejson as json

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'
token = util.prompt_for_user_token(username, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436', redirect_uri='http://localhost:8888/callback/')

if token:
    sp = spotipy.Spotify(auth=token)
    #playlist = sp.user_playlist_create(username, name='asd', public=True)
    p = { "horsedeg": None }
    create_playlist([username], [token], user_playlist_ids=p, desired_length=1234567)
else:
    print("Can't get token for", username)
