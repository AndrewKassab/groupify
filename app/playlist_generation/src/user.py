import sys
from app.playlist_generation.src.track import Track
import spotipy
import spotipy.util as util
import os
import random
from app import app

class user:

    def __init__(self, username, token, playlist_ids):
        self.username = username
        self.token = token
        self.tracks = []
        self.sp = spotipy.Spotify(auth=self.token)

        if len(playlist_ids) > 0:
            self.__retrieve_playlist_tracks(playlist_ids)

        if len(self.tracks) < 50:
            self.__retrieve_most_listened_tracks()

    # Adds tracks from a specified list of playlists into the track pool
    def __retrieve_playlist_tracks(self, playlist_ids):
        for id in playlist_ids:
            offset = 0
            tracks = self.sp.user_playlist_tracks(self.username, id, fields=None, limit = 100, offset = offset, market = None)
            while tracks['next'] and offset <= 9900:
                for j, item in enumerate(tracks['items']):
                    artist_list = [artist['name'] for artist in item['track'].get('artists', [])]
                    track = Track(item['track']['id'], item['track']['name'], artist_list, item['track']['duration_ms'])
                    self.tracks.append(track)
                offset += 100
                tracks = self.sp.user_playlist_tracks(self.username, id, fields=None, limit = 100, offset = offset, market = None)

    def __retrieve_most_listened_tracks(self):
        tracks = self.sp.current_user_top_tracks(limit=50, time_range='short_term')
        for track in tracks['items']:
            artist_list = [artist['name'] for artist in track['artists']]
            self.tracks.append(Track(track['id'], track['name'], artist_list, track['duration_ms']))

    def remove_from_pool(self, tracks):
        for track in tracks:
            self.tracks.remove(track)

    def has_track_saved(self, track_ids):
        if track_ids == []:
            return []
        result = []
        i = 0
        while i < len(track_ids):
            result += self.sp.current_user_saved_tracks_contains(track_ids[i:i+50])
            i += 50
        return result

