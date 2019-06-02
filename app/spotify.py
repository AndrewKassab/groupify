import os, spotipy
from app.flask_spotify_connect import getAuth, refreshAuth, getToken, userInfo

# Client Keys
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

#Port and callback url can be changed or ledt to localhost:5000
PORT = 3000#os.environ['PORT']
CALLBACK_URL = os.environ['CALLBACK_URL']

#Add needed scope from spotify user
SCOPE = "streaming user-read-birthdate user-read-email user-library-modify user-library-read playlist-modify-public playlist-read-collaborative"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, f'{CALLBACK_URL}:{PORT}/callback/', SCOPE)

def getUserToken(code):
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))
    return TOKEN_DATA

def refreshToken(refresh):
    TOKEN_DATA = refreshAuth(refresh)
    return TOKEN_DATA

def getUserInfo(token):
    return userInfo(token)

def getUserPlaylists(token,username):
    sp = spotipy.Spotify(auth=token)
    return sp.user_playlists(username)
