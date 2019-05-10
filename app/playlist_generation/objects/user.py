class User:

    def __init__(self, username):
        self.username = username
        self.saved_tracks = None # List of Type Track
        self.playlists = None # List of Type Playlist
        self.most_listened = None # List of Type Track (Temporarily exclude?)
        __retrieve_saved_tracks(self)
        __retrieve_playlists(self)
        __retrieve_most_listened(self)

    def __retrieve_saved_tracks(self): pass
        self.saved_tracks = # TODO: Retrieve info from api 
    
    def __retrieve_playlists(self): pass
        self.playlists = # TODO: Retrieve info from api 
    
    def __retrieve_most_listened(self): pass
        self.most_listened = # TODO: Retrieve info from api 
    