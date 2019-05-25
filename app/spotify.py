

from app.flask_spotify_auth import getAuth, refreshAuth, getToken

# Client Keys
CLIENT_ID = "539ee5becac647e78e797f9bbe6bd062"
CLIENT_SECRET = "6fc5f4f40b0d4acbbfe01d3ac538a607"

#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "streaming user-read-birthdate user-read-email user-read-private"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, f'{CALLBACK_URL}:{PORT}/callback/', SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))

def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
