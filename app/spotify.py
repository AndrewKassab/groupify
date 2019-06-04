import os, spotipy
from app.flask_spotify_connect import getAuth, refreshAuth, getToken, userInfo

# Client Keys
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

#Port and callback url can be changed or ledt to localhost:5000
PORT = 3000#os.environ['PORT']
CALLBACK_URL = os.environ['CALLBACK_URL']

#Add needed scope from spotify user
SCOPE = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'

#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, CALLBACK_URL, SCOPE)

def getUserToken(code):
    return getToken(code, CLIENT_ID, CLIENT_SECRET, CALLBACK_URL)

def refreshToken(refresh):
    return refreshAuth(refresh, CLIENT_SECRET, CLIENT_ID)

def getUserInfo(token):
    return userInfo(token)

def getUserPlaylists(token,username):
    sp = spotipy.Spotify(auth=token)
    return sp.user_playlists(username)
