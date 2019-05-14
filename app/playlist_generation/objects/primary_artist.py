from artist import Artist

class PrimaryArtist(Artist):

  def __init__(self, artist_id):
    super(self,artist_id)
    self.related_artists = None
    __retrieve_related_artists(self)

    # TODO:
    def __retrieve_related_artists(self): 
        pass
        # Retrieve data from api 
        # Create artist objects()
        # add to self.related_artists

    # TEST: For testing purposes only!
    def add_related_artist(self, artist):
      self.related_artists[artist.artist_id] = artist
