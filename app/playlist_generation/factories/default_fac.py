# This factory generates a playlist assuming no preferences
# or checkboxes have been selected.

from p_factory import PlaylistFactory

class DefaultPlaylistFactory(PlaylistFactory):

    # Filters by related artists ( and genres )?
    def filter_similarities(self):
        return None

    # Lvl 4 filter
    def filter_by_length(self):
        return None