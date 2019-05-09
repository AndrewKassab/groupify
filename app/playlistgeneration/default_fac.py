# This factory generates a playlist assuming no preferences
# or checkboxes have been selected.
# TODO: Complete

from PlaylistFactory import PlaylistFactory

class DefaultPlaylistFactory(PlaylistFactory):

    # Lvl 1 filter
    def filter_intersect(self):
        return None

    # Lvl 1 filter
    def filter_union(self):
        return None

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
