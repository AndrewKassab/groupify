class Tracks:

    def __init__(self, songid):
        self.songid = songid
        self.genre = None
        self.artist = None # Type Artist
        __retrieveGenre(self)
        __retrieveArtist(self)

    def __retrieveGenre(self): pass
        self.genre = # TODO: Request data from api
    
    def __retrieveArtist(self): pass
        self.artist = # Request data from api 
