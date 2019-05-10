class UserArtist(Artist):

  def __init__(self, id):
    super(self,id)
    self.related_artists = None
    __retrieve_related_artists(self)
    __retrieve_top_songs(self)

    def __retrieve_related_artists(self): pass
        # Retrieve data from api 
        # Create artist objects 
        self.related_artists = # TODO: Request data from api
    
    def __retrieve_genre(self): pass
        self.genre = # TODO: Request data from api 

    def __retrieve_top_songs(self): pass
        self.top_songs = # TODO: Request data from api