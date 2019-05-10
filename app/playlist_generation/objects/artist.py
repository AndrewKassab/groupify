class Artist:

    def __init__(self, id):
        self.id = id
        self.genre = None 
        self.related_artists = None # List of type artist
        self.top_songs = None # List of type track
        __retrieve_related_artists(self)
        __retrieve_top_songs(self)

    def __retrieve_related_artists(self): pass
        self.related_artists = # TODO: Request data from api
    
    def __retrieve_genre(self): pass
        self.genre = # TODO: Request data from api 

    def __retrieve_top_songs(self): pass
        self.top_songs = # TODO: Request data from api
