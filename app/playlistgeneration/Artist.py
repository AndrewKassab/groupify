class Artist:

  def __init__(self, id):
    self.id = id
    self.genre = None
    self.relatedArtists = None # List of type artist
    self.topSongs = None # List of type track
    __retrieveRelatedArtists(self)
    __retrieveTopSongs(self)

  def __retrieveRelatedArtists(self):
    self.relatedArtists = # TODO: Request data from api

  def __retrieveGenre(self):
    self.genre = # TODO: Request data from api

  def __retrieveTopSongs(self):
    self.topSongs = # TODO: Request data from api
