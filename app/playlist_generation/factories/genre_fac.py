# This factory generates a playlist when the song pool is narrowed
# down to music relating to specified genres

from p_factory import PlaylistFactory

class UserGenrePlaylistFactory(PlaylistFactory):

    # filter with preference for similar genres
    def filter_similarities(self):
        return None

    # Lvl 4 filter
    def filter_by_length(self):
        return None
