from abc import ABC, abstractmethod
import random
import sys
import copy
from user import User
sys.path.append("../")

class PlaylistFactory(ABC):

    def __init__(self, users, playlists, desired_length):
        # TODO: Construct users?
        self.users = users
        self.desired_length = desired_length
        self.current_length = 0
        self.most_played_tracks = {}
        self.union_tracks = {}
        self.tracks = {}
        self.playlists = playlists
        super().__init__()

    # Creates the playlist by running appropriate methods to filter songs
    def create(self):
        self.__group_union_tracks()
        self.__group_most_played()
        self.__filter_group(self.most_played_tracks)
        self.__filter_group(self.union_tracks)
        self.__filter_by_length()
        self.__combine()
        self.__create_playlist()

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

    # Groups all user's most played tracks and 
    def __group_most_played(self):
        for user in self.users:
            for track in user.most_listened:
                if track.song_id in self.most_played_tracks:
                    self.most_played_tracks[track.song_id].add_user(user)
                    track = self.most_played_tracks[track.song_id]
                else: 
                    self.most_played_tracks[track.song_id] = track

    # Filters by similarities defined by the extending class
    def __filter_group(self,  ) 
        length_cap = ( self.desired_length * percentage ) 
        group_as_list = []
        # Create copy of the group as a list instead of dictionary
        for key, value in .iteritems():
            temp = [key,value]
            group_as_list.append(temp)
        while group_as_list != [] and not (duration > length_cap):
            random_track = random.choice(group_as_list)

    # Combine union list and intersect list
    def __combine(self):

        # Convert both lists to sets
        union_set = set(self.union_tracks)
        common_set = set(self.common_tracks)

        # Merge the sets
        union_set.union(common_set)

        # Finally convert to list
        self.tracks = list(union_set)

    # TODO: Create SPOTIFY playlist object or JSON for spotify
    def __create_playlist(self):
        pass
        # playlist_name = Groupify-DATE
        # playlist_image = groupify album art by default (?)

        # playlist = Playlist( self.tracks , "", "")
        # return playlist or make api calls to create it 
