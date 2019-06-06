from app import app, db
from app.models import *
from app.spotify import *
import uuid, sys, requests
from app.flask_spotify_connect import getAuth, refreshAuth, getToken, userInfo, HEADER
from flask import jsonify, request, abort, Response, redirect
from app.playlist_generation.src.createplaylist import create_playlist, add_to_spotify
from datetime import datetime, timedelta

@app.route('/api/me',methods=['GET'])
def who_am_i():
    auser = authenticate_user(request)

    return response({'user': auser.to_dict(), 'status': 'success'},200)

@app.route('/api/playlists/<int:group_id>/spotify',methods=['POST'])
def add_spotify(group_id):
    auser = authenticate_user(request)

    # Get the group playlist by id
    playlist = Group.query.filter_by(id=group_id).first()

    if playlist is None:
        abort(404)

    tracks = []

    # Get all of the track id's for spotify
    for track in playlist.tracks:
        tracks.append(track.spotify_id)

    playlist_id = add_to_spotify(auser.username, auser.access_token, tracks, playlist.title)

    new_playlist = SpotifyPlaylist(group_id=playlist.id,user_id=auser.id,spotify_id=playlist_id,group=playlist,user=auser)
    db.session.add(new_playlist)
    db.session.commit()

    return response({'spotify_id':playlist_id,'status':'success'},200)

# This is for finding a user's playlists
@app.route('/api/search/playlists/<int:user_id>',methods=['GET'])
def get_playlists(user_id):
    main_user = authenticate_user(request)

    auser = User.query.filter_by(id=user_id).first()
    p_info_dict = getUserPlaylists(main_user.access_token,auser.username)

    playlists = []

    for playlist in p_info_dict['items']:
        playlists.append({'name':playlist['name'],'spotify_id':playlist['id']})

    return response({
        'playlists': playlists,
        'status':'success'
    },200)

# Search for all users, thius prints too much info rn
@app.route('/api/search/users',methods=['GET'])
def search_users():
    authenticate_user(request)

    users = [ \
        {'id': Id, 'name': name, 'username': username} \
        for (Id, name, username) in db.session.query(User.id, User.name, User.username).all() \
    ]

    return response({'users':users},200)

#DONE
@app.route('/api/signup')
def signup():
    response = getUser()

    return redirect(response)

# List playlists
# DONE
@app.route('/api/playlists', methods=['GET'])
def list_playlists():
    auser = authenticate_user(request)

    # The list of playlists to eventually be returned
    playlists = [group.short_details(auser) for group in auser.groups]

    return response({'playlists': playlists, 'status':'success'},200)


# Edit playlist
# DONE
@app.route('/api/playlists/<int:group_id>',methods=['POST'])
def edit_playlist(group_id):

    auser = authenticate_user(request)

    # Get the group from the database
    # and get the name from the request
    group = Group.query.filter_by(id=group_id).first()
    name = request.json.get('name', None)
    visible = request.json.get('visible', None)

    if group is None:
        abort(404)

    updates = {'id': group_id}

    if name is not None:
        group.title = name
        updates['name'] = name

    if visible is not None:
        group.set_visible(auser, visible)
        updates['visible'] = visible

    db.session.commit()

    return response({
        'playlist': updates,
        'status': 'success'
    }, 200)

# Playlist details
@app.route('/api/playlists/<int:group_id>',methods=['GET'])
def get_playlist_details(group_id):

    auser = authenticate_user(request)
    group = Group.query.filter_by(id=group_id).first()

    return response({"playlist": group.full_details(auser),
        "status": "success"
    }, 200)


# Create playlist
@app.route('/api/playlists/create',methods=['POST'])
def create():

    main_user = authenticate_user(request)

    user_ids = request.json['users']
    name = request.json['name']
    duration = request.json['duration']

    # {"<username>": ["<id1>", "<id2>"]}
    user_playlists = request.json['userPlaylists']

    usernames = []
    tokens = []

    user_ids.remove(main_user.id)

    # Need to get auth tokens from users
    # will refresh
    users = [main_user] + User.query.filter(User.id.in_(user_ids)).all()

    for auser in users:
        refresh_if_needed(auser)

        # Make users array
        usernames.append(auser.username)
        tokens.append(auser.access_token)

    db.session.commit()

    # duration comes in minutes
    # this is going to pass back a lot of info in for of track objects I believe

    track_objects = create_playlist(name,usernames,tokens,user_playlists,duration*60000)

    if track_objects is None:
        abort(404)

    tracks = []

    group = Group(title=name,owner=main_user)

    # Make the tracks array and add all tracks to db
    for track_object in track_objects:
        track = Track(
            name=track_object.name,
            duration=track_object.duration / 1000,
            spotify_id=track_object.id,
            artists=" | ".join(track_object.artists),
            group_id=group.id
        )
        tracks.append(track)
        db.session.add(track)

    group.users = users
    group.tracks = tracks
    db.session.add(group)
    db.session.commit()

    return response({
        'playlist':{
            'id': group.id,
            'name': group.title,
            'state': 'complete'
        },
        'status': 'success'
    },200)

# User logout functionality removes the token from the DB
@app.route('/api/logout',methods=['DELETE'])
def logout():

    user = authenticate_user(request)

    token = AuthToken.query.filter_by(token=request.args['token']).first()

    user.auth_tokens.remove(token)
    db.session.delete(token)
    db.session.commit()

    return response('', 200)


@app.route('/api/callback',methods=['POST'])
def callback():

    token_data = getUserToken(request.json['code'])
    userInfo = getUserInfo(token_data[0])

    # Check if it already exists in table
    auser = User.query.filter_by(username=userInfo['id']).first()

    # Create a new uuid token
    userAuthToken = uuid.uuid4()

    auth = None

    expiration = datetime.now() + timedelta(seconds=token_data[3])
    token = token_data[0]
    refresh = token_data[4]

    if auser is None:
        # Make a new user if user is not in table

        auser = User(
            name=userInfo['display_name'],
            username=userInfo['id'],
            access_token=token,
            refresh_token=refresh,
            token_expiration=expiration
        )
        db.session.add(auser)
        db.session.commit()
    else:
        auser.access_token = token
        auser.refresh_token = refresh
        auser.token_expiration = expiration

        db.session.commit()

    auth = AuthToken(user=auser,token=userAuthToken,user_id=auser.id)
    db.session.add(auth)
    db.session.commit()

    app.logger.info(f'{auser.id}')

    if userInfo is None:
        abort(404)

    # Add the Auth token and refresh token to the database
    return response({'token':userAuthToken,'user_id':auser.id},200)


def authenticate_user(req):
    token = AuthToken.query.filter_by(token=req.args['token']).first()

    if token is None:
        abort(401)

    auser = token.user

    if auser is None:
        abort(401)

    # refresh token if needed
    refresh_if_needed(auser)

    return auser


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
        return f'{error.code}'


def response(json,code):
    response = jsonify(json)
    response.status_code = code
    return response


def refresh_token(auser):
    token_data = refreshToken(auser.refresh_token)
    auser.access_token = token_data[0]
    auser.refresh_token = token_data[4]
    auser.token_expiration = datetime.now() + timedelta(seconds=token_data[3])

    db.session.commit()

def refresh_if_needed(user):
    if (user.token_expiration + timedelta(minutes = 5)) < datetime.now():
        # need to refresh the token
        refresh_token(user)
