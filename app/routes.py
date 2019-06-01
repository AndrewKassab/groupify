from app import app, db
from app.models import *
from app.spotify import *

import sys

import datetime

from flask import jsonify, request, abort, Response, redirect

HOME_PAGE = 'http://localhost:3000'
LOGIN_PAGE = 'http://localhost:3000'

# TODO
@app.route('/api/search/playlists/<int:user_id>',methods=['GET'])
def get_playlists():
    user = authenticate_user(request)

    getUserPlaylists(user.auth_tokens,user.username)

@app.route('/api/db/User/clear')
def clear_db():
    db.session.query(User).delete()
    db.session.commit()
    return redirect('/api/signup')


#DONE
@app.route('/api/signup')
def signup():
    response = getUser()

    return redirect(response)

# List playlists
# DONE
@app.route('/api/playlists', methods=['GET'])
def list_playlists():

    user = authenticate_user(request)

    # The list of playlists to eventually be returned
    playlists = []

    # Iterate through all of the user's groups
    for group in user.groups:

        playlists.append({'id': group.id, 'name': group.title, 'state':'done'})

    return response({'playlists': playlists, 'status':'success'},200)


# Edit playlist
# DONE
@app.route('/api/playlists/<int:group_id>',methods=['POST'])
def edit_playlist(group_id):

    user = authenticate_user(request)

    # Get the group from the database
    # and get the name from the request
    group = Group.query.filter_by(id=group_id).first()
    name = request.form['name']

    if group is None or name is None:
        abort(404)

    group.title = name
    db.commit()

    return response({'playlist': {
        'id': group_id,
        'name': name,
        },
        'status': 'success'
    }, 200)

# Playlist details
@app.route('/api/playlists/<int:group_id>',methods=['GET'])
def get_playlist_details(group_id):

    user = authenticate_user(request)

    # TODO
    group = Group.query.filter_by(id=group_id).first()

    tracks = []

    for track in group.tracks:
        tracks.append({'id':track.id,'name':track.name,'artists':track.artists})

    users = []

    for user in group.users:
        users.append({'id':user.id,'name':user.username})

    return response({"playlist": {
        "id": group_id,
        "name": group.title,
        "tracks": tracks,
        "users": users,
        "state": "done"
        },
        "status": "success"
    }, 200)


# Create playlist
# BIG TODO need to work with some of the backend p factory
# people to do this one
@app.route('/api/playlists/create',methods=['POST'])
def create_playlist():

    user = authenticate_user(request)

    # TODO
    return None

# Delete playlist
@app.route('/api/playlists/<int:group_id>',methods=['DELETE'])
def delete_playlist(group_id):

    user = authenticate_user(request)

    return response({'playlists': playlists, 'status':'success'},200)

@app.route('/api/logout',methods=['DELETE'])
def logout():

    user = authenticate_user(request)

    token = AuthToken.query.filter_by(token=request.form[token]).first()
    db.session.delete(token)

    return response(None,200)


@app.route('/api/callback/')
def callback():

    # verify that the callback got a code from the user
    if not 'code' in request.args.keys():
        return redirect(LOGIN_PAGE)

    token_data = getUserToken(request.args['code'])
    userInfo = getUserInfo()

    # Check if it already exists in table
    user = User.query.filter_by(username=userInfo['id']).first()

    if user is None:
        # Make a new user if user is not in table
        user = User(name=userInfo['display_name'],username=userInfo['id'],access_token=token_data[0],refresh_token=str(token_data[1]),token_expiration=datetime.datetime.now()+datetime.timedelta(seconds=token_data[3]))


    if userInfo is None:
        abort(404)

    # Add the Auth token and refresh token to the database
    db.session.add(user)
    db.session.commit()

    return redirect(HOME_PAGE)


def authenticate_user(request):

    if 'token' not in request.form:
        abort(401)

    token = AuthToken.query.filter_by(token=request.form['token']).first()
    user = token.user

    if user is None:
        abort(401)

    # refresh token if needed
    if user.token_expiration >= datetime.datetime.now():
        token_data = refreshToken(3600)
        user.access_token=token_data[0]
        user.refresh_token=token_data[1]
        user.token_expiration=token_data[3]
        db.commit()

    return user


@app.errorhandler(401)
def custom_401(error):
    return std_error_handler(error)


@app.errorhandler(404)
def custom_404(error):
    return std_error_handler(error)


def std_error_handler(error):
    return response({
        'message':f'{get_error_msg(error)}',
        'code':f'{error.code}',
        'status':'error'
    },error.code)


def get_error_msg(error):
    if(error.code==404):
        return '404 MESSAGE'
    if(error.code==401):
        return '401 MESSAGE'
    else:
        return f'{error}'

def response(json,code):
    response = jsonify(json)
    response.status_code = code
    return response
