import settings

class Artist:

    def __init__(self, artist_id):
        self.artist_id = id
        self.genres = None # List of genre ids
        self.top_songs = None # List of songids 
        __retrieve_top_songs(self)

    def __retrieve_top_songs(self):
        # Retrieve info from api
        # add each songid to self.top_songs
        # Gets the top 10 tracks from the artist

        top_songs_list = spotify.artist_top_tracks(self.artist_id)
        self.top_songs = [item['id'] for item in top_songs_list['items']]

    def __retrieve_genres(self):
        # Retrieve info from api 
        # set self.genres

        self.genres = spotify.artist(self.artist_id)['genres']
