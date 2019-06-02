import random
from user import User

class PlaylistFactory():

    def __init__(self, users, desired_length):
        self.users = users
        if desired_length > 3600000:
            self.desired_length = desired_length * 1.15
        self.desired_length = desired_length * 1.25
        self.current_length = 0
        self.tracks = {}

    # creates our playlist
    def create(self, user):
        self.__determine_track_list()
        playlist = user.sp.user_playlist_create(user.username, name='GROUPIFY', public=True)#, description=",".join(usernames))
        track_ids = [t for t in self.tracks]
        user.sp.user_playlist_add_tracks(user.username, playlist['id'], track_ids)

    # determines track list
    def __determine_track_list(self):
        for user in self.users:
            self.__grab_users_tracks(user)
    
    def get_tracks(self):
        return self.tracks

    # Takes tracks from this user's pool for the final track list
    # TODO: Explore edge cases!
    def __grab_users_tracks(self, user):

        max_duration = self.desired_length / len(self.users)
        current_duration = 0
        random.shuffle(user.tracks)

        for track in user.tracks:
            for other_user in self.users:
                if other_user == user:
                    continue
                if other_user.has_track_saved(track.id):
                    if track.id not in self.tracks:
                        self.tracks[track.id] = track
                        user.remove_from_pool(track)
                        current_duration += track.duration
            if current_duration >= max_duration:
                return

        random.shuffle(user.tracks)

        while current_duration < max_duration:
            for track in user.tracks:
                if track.id not in self.tracks:
                    self.tracks[track.id] = track
                    current_duration += track.duration
