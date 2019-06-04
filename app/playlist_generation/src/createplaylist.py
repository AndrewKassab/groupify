from app.playlist_generation.src.user import user
from app.playlist_generation.src.p_factory import PlaylistFactory
import spotipy 
import spotipy.util as util
import os

def create_playlist(name, usernames, tokens, user_playlist_ids, desired_length,
        to_add=True):
    if len(usernames) != len(tokens):
      return None

    users = []
    for username, token in zip(usernames, tokens):
        users.append(user(username, token, user_playlist_ids[username]))

    my_factory = PlaylistFactory(name, users, desired_length)

    # Create the playlist on main user's account
    my_factory.create()

    tracks = my_factory.get_tracks()
    track_ids = []
    for track in tracks:
        track_ids.append(track.id)

    # If user wants to auto-create on spotify
    if to_add is True: 
      add_to_spotify(users[0].username, users[0].token, track_ids, name)

    return tracks

# Creates the playlist on the desired user's account
def add_to_spotify(username, token, tracks_ids, playlist_name):
    sp = spotipy.Spotify(auth = token)
    playlist = sp.user_playlist_create(username, playlist_name, public=True)
    sp.user_playlist_add_tracks(username, playlist['id'], tracks_ids)

