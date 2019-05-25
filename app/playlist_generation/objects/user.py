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
        self.playlists = [] # List of Type Playlist
        self.most_listened = None # Dictionary of Type Track
        self.most_listened_artists = None # Dictionary of Type Artist
        self.__retrieve_playlists()
        self.__retrieve_most_listened()

    # TODO: Retrieve info only for playlists of interest
    def __retrieve_playlists(self):

        # TODO: Fix
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
        for current_playlist in playlists['items']:
            self.playlists.append(Playlist(current_playlist['id'],current_playlist,self.username))

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
