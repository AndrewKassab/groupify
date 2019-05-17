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

    # TODO: Checks if 2 tracks have some similarity or relation
    def is_similar(self, track):
        # Check if the artist that track 2 is by falls under related 
        if self.artist.is_related_artist(track.artist):
            return True
        # Check if the genres are related (??) depending on factory settings
            #return True
        return False