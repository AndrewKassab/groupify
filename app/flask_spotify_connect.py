import base64, json
from flask import jsonify, request, abort, Response, redirect
import requests
from app import app

from urllib.parse import quote

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token'
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

    encoded = base64.urlsafe_b64encode("{}:{}".format(client_id, client_secret).encode())

    headers = {"Content-Type" : HEADER, "Authorization" : "Basic {}".format(encoded)}

    post = requests.post(SPOTIFY_URL_TOKEN, data=body)

    if post is None:
        return False

    return handleToken(json.loads(post.text))

def handleToken(response, refresh=None):
    auth_head = {"Authorization": f'Bearer {response["access_token"]}'}
    refresh_token = refresh or response["refresh_token"]
    app.logger.info(f'refresh token {refresh_token}')
    return [response["access_token"], auth_head, response["scope"], response["expires_in"],refresh_token]

def refreshAuth(refresh,client_secret,client_id):

    app.logger.info(refresh)

    body = {
        "grant_type" : "refresh_token",
        "refresh_token" : refresh
    }

    encoded = base64.urlsafe_b64encode(f'{client_id}:{client_secret}'.encode())

    headers = {'Content-Type': HEADER}

    res = requests.post(
        SPOTIFY_URL_TOKEN, auth=(client_id, client_secret), data=body, headers=headers
    )
    p_back = res.json()

    return handleToken(p_back, refresh)

def userInfo(access_token):

    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    return profile_data
