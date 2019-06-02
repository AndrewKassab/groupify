import sys
sys.path.append('../')
from track import Track
import spotipy
import spotipy.util as util
import os

class User:

    def __init__(self, username, token, playlist_ids = None):
        self.username = username
        self.token = token
        self.tracks = []
        self.sp = spotipy.Spotify(auth=self.token)

        if playlist_ids is not None:
            self.__retrieve_playlist_tracks(playlist_ids)
        self.__retrieve_most_listened_tracks()

    # Adds tracks from a specified list of playlists into the track pool
    def __retrieve_playlist_tracks(self, playlist_ids):
        playlists = self.sp.user_playlists(self.username)
        for id in playlist_ids:
            results = self.sp.user_playlist(self.username, id, fields="tracks,next")
            tracks = results['tracks']
            for j, item in enumerate(tracks['items']):
                track = Track(item['track']['id'], item['track']['duration_ms'])
                self.tracks.append(track)

    def __retrieve_most_listened_tracks(self):
        tracks_obj = self.sp.current_user_top_tracks(limit=50, time_range='medium_term')
        for track in tracks_obj['items']:
            self.tracks.append(Track(track['id'], track['duration_ms']))

    def remove_from_pool(self, track):
        self.tracks.remove(track)

    def has_track_saved(self, track_id):
        return self.sp.current_user_saved_tracks_contains([track_id])
