#import objects.settings
import sys
sys.path.append('../')
from objects.track import Track
from objects.playlist import Playlist
import spotipy
import spotipy.util as util
import os
#from app.playlist_generation.objects.settings import *
#from app.playlist_generation.objects.track import *
#from app.playlist_generation.objects.playlist import *

class User:

    #remove retrieve saved tracks
    def __init__(self, username):
        self.username = username
        self.playlists = [] # List of Type Playlist
        self.most_listened = None # Dictionary of Type Track

        try:
            self.token = util.prompt_for_user_token(self.username)
        except:
            os.remove(f".cache-{self.username}")
            self.token = util.prompt_for_user_token(self.username)

        self.sp = spotipy.Spotify(auth=self.token)

        self.__retrieve_playlists()
        self.__retrieve_most_listened()

    # TODO: Retrieve info only for playlists of interest
    def __retrieve_playlists(self):
        
        # TODO: Fix
        playlists = self.sp.user_playlists(self.username)
        for current_playlist in playlists['items']:
            self.playlists.append(Playlist(current_playlist['id'],current_playlist,self))

    # TODO:
    def __retrieve_most_listened(self):
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened
