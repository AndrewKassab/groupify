class User:

  def __init__(self, username):
    self.username = username
    self.savedTracks = None # List of Type Track
    self.playlists = None # List of Type Playlist
    self.mostListened = None # List of Type Track (Temporarily exclude?)
    __retrieveSavedTracks(self)
    __retrievePlaylists(self)
    __retrieveMostListened(self)

  def __retrieveSavedTracks(self): pass
    self.savedTracks = # TODO: Retrieve info from api 
  
  def __retrievePlaylists(self): pass
    self.playlists = # TODO: Retrieve info from api 
  
  def __retrieveMostListened(self): pass
    self.MostListened = # TODO: Retrieve info from api 