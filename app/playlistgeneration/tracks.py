class Tracks:

    def __init__(self, songid, users):
        self.songid = songid
        self.genre = None
        self.artist = None # Type Artist
        self.users = None # Users who have this track saved
        __retrieve_genre(self)
        __retrieve_artist(self)

    def __retrieve_genre(self): pass
        self.genre = # TODO: Request data from api
    
    def __retrieve_artist(self): pass
        self.artist = # Request data from api 
