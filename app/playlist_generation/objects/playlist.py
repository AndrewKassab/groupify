#import objects.settings

#from app.playlist_generation.objects.settings import *

class Playlist:

    def __init__(self, playlist_id = None, tracks = None, name = None):
        self.playlist_id = playlist_id
        self.tracks = tracks
        self.name = name
        self.time_length = None
        # Generated playlist
        if playlist_id is None:
            # skip retrieving info but set time_length to the sum of track lengths 
        else: 
            self.__retrieve_info()

    # TODO:
    def __retrieve_info(self):
        pass
        # Retrive info from api
        # Add each song_id to self.songs
        # set self.name
        # set self.image
        # set self.time_length

    # TODO:
    def toJson(self):
        pass
        # Generate json data for the playlist?
