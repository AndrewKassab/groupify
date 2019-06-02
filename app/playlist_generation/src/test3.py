
import sys
sys.path.append('../')

import spotipy
import spotipy.util as util
import os



username = sys.argv[1]
scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'
token = util.prompt_for_user_token(username, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')

sp = spotipy.Spotify(auth=token)

playlists = sp.user_playlists(username)
for i in playlists['items']:
    total_duration = 0
    playlist_tracks = {}
    print(i['name']  + "    " + i['id'])
