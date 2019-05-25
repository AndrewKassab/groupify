class Playlist:

    def __init__(self, playlist_obj = None, user):
        self.tracks = {}
        self.duration = 0 
        self.user = user
        self.__retrieve_info(playlist_obj)

    def __retrieve_info(self, playlist_obj):
        total_duration = 0
        playlist_tracks = {}
        results = sp.user_playlist(self.username, i['id'],fields="tracks,next")
        tracks = results['tracks']
        # TODO: Someone check this, Does this syntax work??? 
        for j, item in enumerate(tracks['items']):
            track = Track(item['track'],self.user) 
            total_duration += track.duration
            self.tracks[track.song_id] = track