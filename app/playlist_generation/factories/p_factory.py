# This is an interface for inheriting classes that
# defines the proccess for which a playlist should
# be generated by the groupify app.

from abc import ABC, abstractmethod
import random
import sys
sys.path.append("../")

class PlaylistFactory(ABC):

    def __init__(self, users, desired_length):
        self.users = users
        self.desired_length = desired_length
        self.common_tracks = {}
        self.union_tracks = {}
        self.tracks = {}
        super().__init__()

    # Creates the playlist by running appropriate methods to filter songs
    def create(self):
        self.__union_tracks()
        self.__filter_common_tracks()
        self.__filter_most_played(self.common_tracks)
        self.__filter_most_played(self.__union_tracks)
        self.__filter_similarities()
        self.__filter_by_length()
        self.__combine()
        self.__create_playlist()

    # Create a union of all user's saved tracks
    def __union_tracks(self):
        for user in self.users:
            # avoid duplicates , but make sure to add user to track object
            for track in user.saved_tracks.values():
                if track.song_id in self.union_tracks:
                    self.union_tracks[track.song_id].add_user(user)
                else: 
                    self.union_tracks[track.song_id] = track

    # Create the group of common tracks, remove them from union group
    def __filter_common_tracks(self):
        if len(self.users) == 2 or len(self.users) == 3:
            min_required = 2
        else: 
            min_required = len(self.users)/2 
        for track in self.union_tracks.values():
            if track.amt_saved >= min_required:
                self.common_tracks[track.song_id] = track
                del self.union_tracks[track.song_id]


    # Filter each track group by most played
    def __filter_most_played(self, track_group): 
        most_played = {}    
        time_length = 0
        for track in track_group:
            if track.is_users_most_played():
                most_played[track.song_id] = track
                del track_group[track.song_id]
                time_length = time_length + track.time_length
        # arbitrarily add a few more songs if the group is too short
        while time_length < ( 2 * self.desired_length ):
            random_track = random.choice(list(track_group.values()))
            most_played[random_track.song_id] = random_track
            time_length = time_length + random_track.time_length


    # Filters by similarities defined by the extending class
    @abstractmethod
    def __filter_similarities(self): 
        pass

    # Lvl 4 filter
    # TODO:
    @abstractmethod
    def __filter_by_length(self): 
        pass

    # Combine union list and intersect list
    def __combine(self):

        # Convert both lists to sets
        union_set = set(self.union_tracks)
        common_set = set(self.common_tracks)

        # Merge the sets
        union_set.union(common_set)

        # Finally convert to list
        self.tracks = list(union_set)

    def __create_playlist(self):

        # TODO:
        # playlist_name = Groupify-DATE
        # playlist_image = groupify album art by default (?)

        playlist = Playlist( self.tracks , "", "")
        return playlist
