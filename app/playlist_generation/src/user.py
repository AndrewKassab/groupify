import sys
sys.path.append('../')
from track import Track
import spotipy
import spotipy.util as util
import os

class User:

    def __init__(self, username, token, playlist_ids = None):
        self.username = username
        self.token = token;
        self.tracks = []
        self.sp = spotipy.Spotify(auth=self.token)

        if playlist_ids is not None:
            self.__retrieve_playlist_tracks(playlist_ids)
        self.__retrieve_most_listened_tracks('medium_term')

    def __retrieve_playlist_tracks(self, playlist_ids):
        playlists = self.sp.user_playlists(self.username)
        for id in playlist_ids:
            tracks = self.sp.user_playlist(self.username, id, fields="tracks,next")
            for j, item in enumerate(tracks['items']):
                track = Track(item['track']['id'], item['track']['duration_ms'])
                self.tracks.append(track)

    def __retrieve_most_listened_tracks(self, range):
        tracks_obj = self.sp.current_user_top_tracks(limit=50, time_range=range)
        for track in tracks_obj['items']:
            self.tracks.append(Track(track['id'], track['duration_ms']))

    # Removes a track from the track pool (after it is already added)
    def remove_from_pool(self, track):
        self.tracks.remove(track)

    def has_track_saved(self, track_id):
        return self.sp.current_user_saved_tracks_contains(track_id)
