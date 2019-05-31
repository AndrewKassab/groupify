import random
from user import User

class PlaylistFactory():

    def __init__(self, users, desired_length):
        self.users = users
        self.desired_length = desired_length * 1.50
        self.current_length = 0
        self.tracks = {}

    # creates our playlist
    def create(self, user):
        self.__determine_track_list()

        # TODO: 
        # playlist_name = GROUPIFY-CURR_DATE
        # playlist_description = username1, username2,for each user in self.users
        # call API to create playlist on passed in user's account
        # (remember that sp is present under user as a variable)
        # add each track.id in self.tracks to the playlist
        usernames = [u.username for u in self.users]
        playlist_id = user.sp.user_playlist_create(user.username, name='GROUPIFY', public=True, description=",".join(usernames))
        track_ids = [t.id for t in self.tracks]
        user.sp.user_playlist_add_tracks(user.username, playlist_id, track_ids)

    # determines track list
    def __determine_track_list(self):
        for user in self.users: 
            self.__grab_users_tracks(user)

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
