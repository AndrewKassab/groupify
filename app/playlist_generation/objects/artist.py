# Requires access to Spotify() object
class Artist:

    def __init__(self, artist_id):
        self.artist_id = id
        self.genres = None # List of genres
        self.top_songs = None # List of songids 
        __retrieve_top_songs(self)

    # TODO:
    def __retrieve_top_songs(self):
        pass
        # Retrieve info from api
        # add each songid to self.top_songs
        # Limit of 50 songs, can use 'short_term' 'medium_term' and 'long_term'

        # top_songs_list = sp.current_user_top_tracks(limit=50, time_range='long_term') # API call: returns dict of song list info
        # self.top_songs =[item['id'] for item in top_songs_list['items']] # Return the list of song ids

    # TODO:
    def __retrieve_genres(self):
        pass
        # Retrieve info from api 
        # set self.genre

        # self.genres = artist(self.artist_id)['genres'] # API call: returns list of genre ids
