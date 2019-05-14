import settings
from track import Track
from playlist import Playlist

class User:

    def __init__(self, username):
        self.username = username
        self.saved_tracks = None # Dictionary of Type Track
        self.playlists = None # List of Type Playlist
        self.most_listened = None # Dictionary of Type Track
        __retrieve_saved_tracks(self)
        __retrieve_playlists(self)
        __retrieve_most_listened(self)

    # TODO:
    def __retrieve_saved_tracks(self): 
        pass
        # Retrieve info from api
        # For each songid create a track object(songid, self)
        # add each track to self.tracks

    # TODO: 
    def __retrieve_playlists(self): 
        pass
        # Retrieve info from api
        # For each playlist create a playlist object(playlist_id)
        # *** for every songId in the playlist, retrieve its value pair 
        # from self.saved_tracks instead of creating a new object
        # add each playlist to self.playlists
    
    # TODO:
    def __retrieve_most_listened(self, timeRange): 
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened

    # Check if the specific track is a most listened to track
    def is_most_listened(track):
        if track.song_id in self.most_listened.values():
            return True
        return False
    
