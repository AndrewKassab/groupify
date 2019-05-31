import sys
sys.path.append('../')
from objects.user import *
from objects.artist import Artist

#from app.playlist_generation.objects.settings import *
#from app.playlist_generation.objects.primary_artist import *

class Track:

    def __init__(self, id, duration):
        self.id = id 
        self.amt_saved = 1
        self.duration = duration

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
