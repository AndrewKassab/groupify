import settings

class Playlist:

    def __init__(self, playlist_id, tracks=None, name=None, image=None, time_length=None):
        self.playlist_id = playlist_id
        self.tracks = tracks 
        self.name = name
        self.image = image
        self.time_length = time_length
        # For pre-existing user playlists
        if tracks is None:
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
