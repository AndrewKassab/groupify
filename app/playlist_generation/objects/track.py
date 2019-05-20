#import objects.settings

#from app.playlist_generation.objects.settings import *
#from app.playlist_generation.objects.primary_artist import *

class Track:

    def __init__(self, song_id, users,artist_name,track_duration, name):
        self.song_id = song_id
        #self.genres = None
        self.name = name
        self.artist = artist_name # Type Artist
        self.users = users # Users who have this track saved
        self.amt_saved = len(users)
        self.time_length = track_duration
        self.mp_priority = 0

    # Add a user to the list of users who have this track saved
    def add_user(self, newuser):
        self.users = self.users + newuser
        self.amt_saved = len(self.users)

    # Check if this track is a most played track by any of its users
    def is_users_most_played(self):
        #for user in self.users:
        #    if user.is_most_listened(self)
        #        return True
        return False
