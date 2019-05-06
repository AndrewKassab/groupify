class User:

  def __init__(self, username):
    self.username = username
    self.savedTracks = none # List of Type Track
    self.playlists = none # List of Type Playlist
    self.mostListened = none # List of Type Track (Temporarily exclude?)
    __retrieveSavedTracks(self)
    __retrievePlaylists(self)
    __retrieveMostListened(self)

  def __retrieveSavedTracks(self):
    self.savedTracks = # TODO: Retrieve info from api 
  
  def __retrievePlaylists(self):
    self.playlists = # TODO: Retrieve info from api 
  
  def __retrieveMostListened(self):
    self.MostListened = # TODO: Retrieve info from api 