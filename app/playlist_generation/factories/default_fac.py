# This factory generates a playlist assuming no preferences
# or checkboxes have been selected.

from PlaylistFactory import PlaylistFactory

class DefaultPlaylistFactory(PlaylistFactory):

    def create(self):
        __union_tracks()
        __squish_tracks()
        __filter_common_tracks(self)
        __filter_intersect_most_played(self)
        __filter_union_most_played(self)
        __filter_union_similarities(self)
        __filter_by_length(self)
        combine(self)
        create_playlist()
        return self.playlist

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