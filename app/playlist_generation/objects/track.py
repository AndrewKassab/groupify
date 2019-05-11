class Track:

    def __init__(self, song_id, users):
        self.song_id = songid
        self.genre = None
        self.artist = None # Type Artist
        self.users = users # Users who have this track saved
        self.amt_saved = len(users)
        self.time_length = None
        self.mp_priority = 0
        __retrieve_genre(self)
        __retrieve_artist(self)

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
        self.amt_saved = len(users)

    # Check if this track is a most played track by any of its users
    def is_users_most_played(self):
        for user in users:
            if user.is_most_listened(this):
                return True
        return False
