class Tracks:

    def __init__(self, songid, users):
        self.songid = songid
        self.genre = None
        self.artist = None # Type Artist
        self.users = [] # Users who have this track saved
        self.amt_saved = len(users)
        __retrieve_genre(self)
        __retrieve_artist(self)

    def __retrieve_genre(self): pass
        self.genre = # TODO: Request data from api
    
    def __retrieve_artist(self): pass
        self.artist = # Request data from api 

    def add_users(self, newusers):
        self.users = self.users + newusers
        self.amt_saved = len(users)
