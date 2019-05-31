from p_factory import PlaylistFactory

class PooledFactory(PlaylistFactory):

    def __init__(self, users, playlists, desired_length):
        self.super(users,desired_length)
        self.playlists = playlists
        self.union_tracks = {}
        
    def __create(self):
        self.__group_union_tracks()
        self.__group_most_played()
        self.__filter_group(self.union_tracks, .5)
        self.__filter_group(self.most_played_tracks, .5)

    # Create a union of all tracks present in the playlists presented
    def __group_union_tracks(self):
        for playlist in self.playlists:
            # avoid duplicates , but make sure to add user to track object
            for track in playlist.tracks:
                if track.song_id in self.union_tracks:
                    self.union_tracks[track.song_id].add_user(playlist.user)
                else: 
                    self.union_tracks[track.song_id] = track
        # TODO: Check to make sure the track pool is >= desired length?