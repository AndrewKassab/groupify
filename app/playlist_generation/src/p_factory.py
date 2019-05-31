from abc import ABC, abstractmethod
import random
import sys
import copy
from user import User
sys.path.append("../")

class PlaylistFactory(ABC):

    def __init__(self, users, desired_length):
        self.users = users
        self.desired_length = desired_length * 1.25
        self.current_length = 0
        self.most_played_tracks = {}
        self.tracks = {}
        super().__init__()

    # Creates the playlist by running appropriate methods to filter songs
    def __create(self):
        self.__group_most_played()
        self.__filter_group(self.most_played_tracks, 1)
        self.__create_playlist()

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
    def __filter_group(self, track_group , percentage):
        length_cap = ( self.desired_length * percentage ) 
        group_as_list = []
        # Create copy of the group as a list instead of dictionary
        for key, value in track_group.iteritems():
            temp = [key,value]
            group_as_list.append(temp)
        while group_as_list != [] and not (duration > length_cap):
            random_track = random.choice(group_as_list)

    # TODO: Create SPOTIFY playlist object or JSON for spotify
    def __create_playlist(self):
        pass
        # playlist_name = Groupify-DATE
        # playlist_image = groupify album art by default (?)

        # playlist = Playlist( self.tracks , "", "")
        # return playlist or make api calls to create it 
