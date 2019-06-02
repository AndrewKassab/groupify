import base64, json
from flask import jsonify, request, abort, Response, redirect
import requests
from app import app

from urllib.parse import quote

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'
HEADER = 'application/x-www-form-urlencoded'

SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


def getAuth(client_id, redirect_uri, scope):
    data = "{}client_id={}&response_type=code&redirect_uri={}&scope={}&show_dialog=true".format(SPOTIFY_URL_AUTH, client_id, redirect_uri, scope)
    return data

def getToken(code, client_id, client_secret, redirect_uri):
    body = {
        "grant_type": 'authorization_code',
        "code" : str(code),
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    encoded = base64.urlsafe_b64encode("{}:{}".format(client_id, client_secret).encode())#.decode()

    headers = {"Content-Type" : HEADER, "Authorization" : "Basic {}".format(encoded)}

    post = requests.post(SPOTIFY_URL_TOKEN, data=body)

    if post is None:
        return False

    return handleToken(json.loads(post.text))

def handleToken(response):
    auth_head = {"Authorization": "Bearer {}".format(response["access_token"])}
    return [response["access_token"], auth_head, response["scope"], response["expires_in"],response["refresh_token"]]

def refreshAuth(refresh):

    body = {
        "grant_type" : "refresh_token",
        "refresh_token" : refresh
    }

    post_refresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
    p_back = json.dumps(post_refresh.text)

    return handleToken(p_back)

def userInfo(access_token):

    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    return profile_data
