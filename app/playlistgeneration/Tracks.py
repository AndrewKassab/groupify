class Tracks:

  def __init__(self, songid):
    self.songid = songid
    self.genre = none
    self.artist = none # Type Artist
    __retrieveGenre(self)
    __retrieveArtist(self)

  def __retrieveGenre(self):
    self.genre = # TODO: Request data from api
  
  def __retrieveArtist(self):
    self.artist = # Request data from api 