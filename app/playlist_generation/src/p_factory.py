import random
from app.playlist_generation.src.user import user

class PlaylistFactory():

    def __init__(self, name, users, desired_length):
        self.name = name
        self.users = users
        self.desired_length = desired_length * 1.05
        self.current_length = 0
        self.tracks = {}

    # creates our playlist
    def create(self, user):
        self.__determine_track_list()
        playlist = user.sp.user_playlist_create(user.username, name=self.name, public=True)#, description=",".join(usernames))
        track_ids = [t for t in self.tracks]
        user.sp.user_playlist_add_tracks(user.username, playlist['id'], track_ids)

    # determines track list
    def __determine_track_list(self):
        for user in self.users:
            self.__grab_users_tracks(user)

    def get_tracks(self):
        return self.tracks

    def get_track_objects(self):
        tracks = []
        for id, track in self.tracks.items():
            tracks.append(track)
        return tracks


    # Takes tracks from this user's pool for the final track list
    def __grab_users_tracks(self, user):
        max_duration = self.desired_length / len(self.users)
        current_duration = 0

        random.shuffle(user.tracks)

        if len(self.users) > 3:
            amt_must_saved = len(self.users)/2
        else:
            amt_must_saved = 2

        to_remove_from_pool = []
        track_ids = []
        for track in user.tracks:
            track_ids.append(track.id)
        for other_user in self.users:
            if other_user == user:
                continue
            tracks_saved_list = other_user.has_track_saved(track_ids)
            for i in range(0, len(tracks_saved_list)):
                if tracks_saved_list[i] is True:
                    user.tracks[i].increment_amt_saved()
        
        while amt_must_saved > 0:
            for track in user.tracks:
                if track.amt_saved >= amt_must_saved:
                    if track.id not in self.tracks:
                        self.tracks[track.id] = track
                        current_duration += track.duration
                    to_remove_from_pool.append(track)
                if current_duration >= max_duration:
                    return
            user.remove_from_pool(to_remove_from_pool)
            amt_must_saved -= 1
