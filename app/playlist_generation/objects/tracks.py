class Tracks:

    def __init__(self, songid, users):
        self.songid = songid
        self.genre = None
        self.artist = None # Type Artist
        self.users = users # Users who have this track saved
        self.amt_saved = len(users)
        self.time_length = None
        __retrieve_genre(self)
        __retrieve_artist(self)

    def __retrieve_genre(self): pass
        # Retrieve genre 
    
    def __retrieve_artist(self): pass
        self.artist = # Request data from api 
    
    def __retrieve_track_length(self): pass
        self.time_length = # Data from api

    def add_users(self, newusers):
        self.users = self.users + newusers
        self.amt_saved = len(users)

    def get_priority(self): 
        return priority

    def is_users_most_played(self)
