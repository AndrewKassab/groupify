import base64, json
from flask import jsonify, request, abort, Response, redirect
import requests

from urllib.parse import quote

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'
HEADER = 'application/x-www-form-urlencoded'
REFRESH_TOKEN = ''

def getAuth(client_id, redirect_uri, scope):
    data = "{}client_id={}&response_type=code&redirect_uri={}&scope={}".format(SPOTIFY_URL_AUTH, client_id, redirect_uri, scope)
    return data

def getToken(code, client_id, client_secret, redirect_uri):
    body = {
        "grant_type": 'authorization_code',
        "code" : str(code),
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    encoded = base64.urlsafe_b64encode("{}:{}".format(client_id, client_secret).encode()).decode()

    headers = {"Content-Type" : HEADER, "Authorization" : "Basic {}".format(encoded)}

    post = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=headers)

    if post is None:
        return False

    return handleToken(json.loads(post.text))

def handleToken(response):

    print("This is the response: !!!!!!!! ")

    auth_head = {"Authorization": "Bearer {}".format(response["access_token"])}
    REFRESH_TOKEN = response["refresh_token"]
    return [response["access_token"], auth_head, response["scope"], response["expires_in"]]

def refreshAuth():
    body = {
        "grant_type" : "refresh_token",
        "refresh_token" : REFRESH_TOKEN
    }

    post_refresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
    p_back = json.dumps(post_refresh.text)

    return handleToken(p_back)
