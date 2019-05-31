import sys
sys.path.append('../')
from track import Track
import spotipy
import spotipy.util as util
import os

class User:

    def __init__(self, username, playlist_ids = None):
        self.username = username
        self.num_songs_included = 0
        self.tracks = {}

        try:
            self.token = util.prompt_for_user_token(self.username)
        except:
            os.remove(f".cache-{self.username}")
            self.token = util.prompt_for_user_token(self.username)

        self.sp = spotipy.Spotify(auth=self.token)

        if playlist_ids is not None:
            self.__retrieve_playlist_tracks(playlist_ids)
        
        self.__retrieve_most_listened()

    def __retrieve_playlist_tracks(self, playlist_ids):
        
        # TODO: Change to only retrieve the playlist_ids instead of all
        playlists = self.sp.user_playlists(self.username)
        for current_playlist in playlists['items']:
            tracks = self.sp.user_playlist(self.username, current_playlist['id'], fields="tracks,next")
            for j, item in enumerate(tracks['items']):
                track = Track(item['track']['id'], item['track']['duration_ms'])
                self.tracks[track.id] = track

    # TODO:
    def __retrieve_most_listened(self):
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened
