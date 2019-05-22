#import objects.settings
import sys
sys.path.append('../')
from objects.track import Track
from objects.playlist import Playlist

#from app.playlist_generation.objects.settings import *
#from app.playlist_generation.objects.track import *
#from app.playlist_generation.objects.playlist import *

class User:

    #remove retrieve saved tracks

    def __init__(self, username):
        self.username = username
        self.saved_tracks = {} # Dictionary of Type Track
        self.playlists = [] # List of Type Playlist
        self.most_listened = None # Dictionary of Type Track

        self.__retrieve_playlists()
        self.__retrieve_most_listened()

    # TODO:
    def __retrieve_playlists(self):
        # Retrieve info from api
        # For each playlist create a playlist object(playlist_id)
        # *** for every songId in the playlist, retrieve its value pair
        # from self.saved_tracks instead of creating a new object
        # add each playlist to self.playlists
        #Currently adds all playlists as objects, and adds all track names and ids to trackName_id
        import spotipy
        import spotipy.util as util
        import os

        try:
            token = util.prompt_for_user_token(self.username)
        except:
            os.remove(f".cache-{self.username}")
            token = util.prompt_for_user_token(self.username)
        sp = spotipy.Spotify(auth=token)

        playlists = sp.user_playlists(self.username)
        for i in playlists['items']:
                total_duration = 0
                playlist_tracks = {}
                results = sp.user_playlist(self.username, i['id'],fields="tracks,next")
                tracks = results['tracks']
                for j, item in enumerate(tracks['items']):
                    track = item['track']
                    track_duration = track['duration_ms']
                    total_duration += track_duration

                    artist_name = track['artists'][0]['name']

                    song = Track(track['id'],self.username,artist_name,track_duration,track['name'])
                    self.saved_tracks.update({track['id']:song})
                    playlist_tracks.update({track['id']:song})
                self.playlists.append(Playlist(i['id'],playlist_tracks,i['name'],total_duration))

        #view songs in saved tracks
    #    for i in self.saved_tracks.values():
    #        print(i)
        #
        # for i in self.playlists:
        #     print("Playlist:" + "  Id:" + i.playlist_id + "   Title:" + i.name)
        #     for j,k in i.tracks.items():
        #         print("Id:" +j + "   Title:" + k)
        #     print()



    # TODO:
    def __retrieve_most_listened(self):
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened

    # Check if the specific track is a most listened to track
    def is_most_listened(self,track):
        if track.song_id in self.most_listened.values():
            return True
        return False
