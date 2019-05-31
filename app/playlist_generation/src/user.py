import sys
sys.path.append('../')
from track import Track
import spotipy
import spotipy.util as util
import os

class User:

    def __init__(self, username, playlist_ids = None):
        self.username = username
        self.tracks = []

        try:
            self.token = util.prompt_for_user_token(self.username)
        except:
            os.remove(f".cache-{self.username}")
            self.token = util.prompt_for_user_token(self.username)

        self.sp = spotipy.Spotify(auth=self.token)

        if playlist_ids is not None:
            self.__retrieve_playlist_tracks(playlist_ids)
        self.__retrieve_most_listened_tracks()

    def __retrieve_playlist_tracks(self, playlist_ids):
        
        # TODO: Change to only retrieve the playlist_ids instead of all
        playlists = self.sp.user_playlists(self.username)
        for current_playlist in playlists['items']:
            tracks = self.sp.user_playlist(self.username, current_playlist['id'], fields="tracks,next")
            for j, item in enumerate(tracks['items']):
                track = Track(item['track']['id'], item['track']['duration_ms'])
                self.tracks.append(track)

    # TODO:
    def __retrieve_most_listened_tracks(self):
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened

    # Removes a track from the track pool (after it is already added)
    def remove_from_pool(self, track):
        self.tracks.remove(track)

    # TODO:
    def has_track_saved(self, track_id):
        pass
        # TODO: Do API call to check if this user has this track saved
        # If so, just return True
        # otherwise, return False
    