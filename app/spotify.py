import os
from app.flask_spotify_connect import getAuth, refreshAuth, getToken, userInfo

# Client Keys
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

#Port and callback url can be changed or ledt to localhost:5000
PORT = os.environ['PORT']
CALLBACK_URL = os.environ['CALLBACK_URL']

#Add needed scope from spotify user
SCOPE = "streaming user-read-birthdate user-read-email user-read-private user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, f'{CALLBACK_URL}:{PORT}/callback/', SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))
    return TOKEN_DATA

def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()
    return TOKEN_DATA

def getAccessToken():
    return TOKEN_DATA

def getUserInfo():
    return userInfo(getAccessToken())
