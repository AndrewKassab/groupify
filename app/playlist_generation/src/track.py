import sys
sys.path.append('../')
from objects.user import *
from objects.artist import Artist

#from app.playlist_generation.objects.settings import *
#from app.playlist_generation.objects.primary_artist import *

class Track:

    def __init__(self, track_obj, user):
        self.song_id = None
        self.name = None
        self.artists = [] # Type Artist
        self.users = [user] # Users who have this track saved
        self.amt_saved = 1
        self.duration = 0
        self.__retrieve_info(track_obj)

    def __retrieve_info(self, track_obj):
        self.song_id = track_obj['id']
        self.name = track_obj['name']
        self.duration = track_obj['duration_ms']
        for artist in track_obj['artists']:
            self.artists.append(Artist(artist))

    # Add a user to the list of users who have this track saved
    def add_user(self, newuser):
        self.users = self.users + newuser
        self.amt_saved += 1
