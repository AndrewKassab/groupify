from app.playlist_generation.objects.settings import *
from app.playlist_generation.objects.primary_artist import *

class Track:

    def __init__(self, song_id, users):
        self.song_id = song_id
        self.genres = None
        self.artist = None # Type Artist
        self.users = users # Users who have this track saved
        self.amt_saved = len(users)
        self.time_length = None
        self.mp_priority = 0
        self.__retrieve_artist()
        self.__retrieve_genres()

    # TODO:
    def __retrieve_genres(self): 
        pass
        # Retrieve info from api
        # set self.genres
        self.genres = self.artist.genres
    
    # TODO:
    def __retrieve_artist(self): 
        pass
        # Retrieve info from api
        # Create PrimaryArtist object(artist_id)
        # set self.artist
        self.artist = PrimaryArtist(spotify.track(self.song_id)['artists'][0]['id'])   
    
    # TODO:
    def __retrieve_track_length(self): 
        pass
        # Retrieve info from api
        # set self.time_length

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
