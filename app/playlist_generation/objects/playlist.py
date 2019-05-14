import settings

class Playlist:

    def __init__(self, playlist_id, songs=None, name=None, image=None, time_length=None):
        self.playlist_id = playlist_id
        self.songs = songs
        self.name = name
        self.image = image
        self.time_length = time_length
        if songs is None:
            __retrieve_info(self)

    # TODO:
    def __retrieve_info(self):
        pass
        # Retrive info from api 
        # Add each song_id to self.songs 
        # set self.name
        # set self.image
        # set self.time_length

    # TODO:
    def toJson():
        pass
        # Generate json data for the playlist?
