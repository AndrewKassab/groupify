# This factory generates a playlist when the song pool is narrowed
# down to music from specific pre-existing playlists

from p_factory import PlaylistFactory

class NarrowedPlaylistFactory(PlaylistFactory):
    
    # TODO: Override union_tracks to only takes tracks from desired playlists
    def __union_tracks(self):
        pass

    def filter_similarities(self):
        return None

    # Lvl 4 filter
    def filter_by_length(self):
        return None
