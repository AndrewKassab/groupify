import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


#Adds bands and genres to the sets band, genres
def add_bands_genres(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        name = track['artists'][0]['name']
        bands.add(name)

        result = spotifyObject.search(name,1,0,"artist")
        artist = result['artists']['items'][0]
        for j in artist['genres']:
            genres.add(j)

#searches user and grabs playlist and iterates through it, works for one playlist currently
def search_playlist():
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print (playlist['name'])
                print( '  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                add_bands_genres(tracks)

                while tracks['next']:
                    tracks = sp.next(tracks)
                    add_bands_genres(tracks)
    else:
        print ("Can't get token for", username)


username = sys.argv[1]

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)


spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()

bands = set()
genres = set()
search_playlist()

print(len(bands))
print(bands)

print()

print(len(genres))
print(genres)
