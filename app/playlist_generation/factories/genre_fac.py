# This factory generates a playlist when the song pool is narrowed
# down to music relating to specified genres

from PlaylistFactory import PlaylistFactory

class UserGenrePlaylistFactory(PlaylistFactory):

    # Lvl 2 filter
    def filter_intersect_most_played(self):
        return None

    # Lvl 2 filter
    def filter_union_most_played(self):
        return None

    # Lvl 3 filter
    def filter_union_similarities(self):
        return None

    # Lvl 4 filter
    def filter_by_length(self):
        return None
