import objects.settings
import sys
sys.path.append('../')
from objects.track import Track
from objects.playlist import Playlist

class User:

    def __init__(self, username):
        self.username = username
        self.saved_tracks = None # Dictionary of Type Track
        self.playlists = [] # List of Type Playlist
        self.most_listened = None # Dictionary of Type Track

        self.trackName_id = [] #For testing

        self.__retrieve_saved_tracks()
        self.__retrieve_playlists()
        self.__retrieve_most_listened()

    # TODO:
    def __retrieve_saved_tracks(self):
        pass
        # Retrieve info from api
        # For each songid create a track object(songid, self)
        # add each track to self.tracks

    # TODO:
    def __retrieve_playlists(self):
        # Retrieve info from api
        # For each playlist create a playlist object(playlist_id)
        # *** for every songId in the playlist, retrieve its value pair
        # from self.saved_tracks instead of creating a new object
        # add each playlist to self.playlists


        #Currently adds all playlists as objects, and adds all track names and ids to trackName_id
        import spotipy
        import spotipy.util as util
        import os

        try:
            token = util.prompt_for_user_token(self.username)
        except:
            os.remove(f".cache-{self.username}")
            token = util.prompt_for_user_token(self.username)
        sp = spotipy.Spotify(auth=token)

        
        playlists = sp.user_playlists(self.username)
        for i in playlists['items']:
                self.playlists.append(i)
                results = sp.user_playlist(self.username, i['id'],fields="tracks,next")
                tracks = results['tracks']
                for j, item in enumerate(tracks['items']):
                    track = item['track']
                    s = "track: "+ track['name'] + " , id: " + track['id']
                    self.trackName_id.append(s)

        #view songs and ids in all playlists
        #for i in self.trackName_id:
        #    print(i)


    # TODO:
    def __retrieve_most_listened(self):
        pass
        # Retrieve info from api
        # For each song_id key, find its corresponding value object in self.saved_tracks
        # and add it to self.most_listened

    # Check if the specific track is a most listened to track
    def is_most_listened(self,track):
        if track.song_id in self.most_listened.values():
            return True
        return False
