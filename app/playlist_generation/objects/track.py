import settings

class Track:

    def __init__(self, song_id, users):
        self.song_id = song_id
        self.genre = None
        self.artist = None # Type Artist
        self.users = users # Users who have this track saved
        self.amt_saved = len(users)
        self.time_length = None
        self.mp_priority = 0 # indicated how important a song is to include
        self.__retrieve_genre()
        self.__retrieve_artist()

    # TODO:
    def __retrieve_genre(self): 
        pass
        # Retrieve info from api
        # set self.genre
    
    # TODO:
    def __retrieve_artist(self): 
        pass
        # Retrieve info from api
        # Create PrimaryArtist object(artist_id)
        # set self.artist
    
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
        for user in self.users:
            if user.is_most_listened(self)
                self.priority += 1
        if priority >= 1:
            return True
        else:
            return False

    # Checks if an artist is a related artist to the creator of this track
    def is_related_artist(self, artist):
        for current_artist in self.artists:
            if self.artist.is_related_artist(artist):
                return True 
        return False