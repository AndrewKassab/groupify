# This factory generates a playlist assuming no preferences
# or checkboxes have been selected.

from p_factory import PlaylistFactory

class DefaultPlaylistFactory(PlaylistFactory):

    def create(self):
        self.__union_tracks()
        self.__filter_common_tracks()
        self.__filter_most_played(self.common_tracks)
        self.__filter_most_played(self.__union_tracks)
        self.__filter_union_similarities()
        self.__filter_by_length()
        self.__combine()
        self.__create_playlist()

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