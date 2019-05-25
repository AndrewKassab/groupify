#import objects.settings

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
        self.mp_priority = 0 # indicated how important a song is to include
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

    # Check if this track is a most played track by any of its users
    def is_users_most_played(self):
        for user in self.users:
            if user.is_most_listened(self)
                self.priority += 1
        if priority >= 1:
            return True
        else:
            return False

    # TODO: Checks if 2 tracks have some similarity or relation
    def is_similar(self, track):
        # Check if the artist that track 2 is by falls under related 
        if self.artist.is_related_artist(track.artist):
            return True
        # Check if the genres are related (??) depending on factory settings
            #return True
        return False
