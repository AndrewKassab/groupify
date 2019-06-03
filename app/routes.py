from app import app, db
from app.models import *
from app.spotify import *
import uuid, sys, requests, datetime
from app.flask_spotify_connect import getAuth, refreshAuth, getToken, userInfo, HEADER
from flask import jsonify, request, abort, Response, redirect
from app.playlist_generation.src.track import Track


# This is for finding a user's playlists
@app.route('/api/search/playlists/<int:user_id>',methods=['GET'])
def get_playlists(user_id):
    main_user = authenticate_user(request)

    user = User.query.filter_by(id=user_id).first()
    p_info_dict = getUserPlaylists(main_user.access_token,user.username)

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

    users = []

    users_db = User.query.all()
    for user in users_db:
        users.append({'name':user.name,'username':user.username,'id':user.id,'auth_token':AuthToken.query.filter_by(user_id=user.id).first().token,'access_token':user.access_token,'refresh':user.refresh_token})

    return response({'users':users},200)

@app.route('/api/db/User/clear')
def clear_db():
    users = User.query.all()

    for user in users:
        for auth_token in user.auth_tokens:
            db.session.delete(auth_token)

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
    name = request.json['name']

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
@app.route('/api/playlists/create',methods=['POST'])
def create():

    main_user = authenticate_user(request)

    user_ids = request.json['users']
    name = request.json['name']
    playlists = request.json['playlists']
    duration = request.json['duration']

    usernames = []
    users = []
    tokens = []

    # Need to get auth tokens from users
    # will refresh
    for user_id in user_ids:
        user = User.query.filter_by(id=user_id).first()
        if user.token_expiration > datetime.datetime.now():
             # need to refresh the token
            refresh_token(user)

        # Make users array
        users.append(user)
        usernames.append(user.username)
        tokens.append(user.access_token)

    # duration comes in minutes
    # this is going to pass back a lot of info in for of track objects I believe
    tracks_objects = create_playlist(name,usernames,tokens,playlists,duration*60000)

    if track_objects is None:
        abort(404)

    tracks = []

    group = Group(title=name,owner=main_user)

    # Make the tracks array and add all tracks to db
    for track_object in track_objects:
        track = Track(name=track_object.name,duration=track_object.duration/60000,spotify_id=track_object.id,artists=track_object.artists,group_id=group.id)
        tracks.append(track)
        db.session.add(track)

    group.users = users
    group.tracks = tracks
    db.session.add(group)
    db.session.commit()

    return response({
        'playlist':{
            'id': group.id,
            'name': group.name,
            'state': 'complete'
        },
        'status': 'success'
    },200)

# Delete playlist
@app.route('/api/playlists/<int:group_id>',methods=['DELETE'])
def delete_playlist(group_id):

    user = authenticate_user(request)

    group = Group.query.filter_by(id=group_id).first()

    for track in group.tracks:
        db.session.delete(track)

    db.session.delete(group)
    db.session.commit()

    return response({'status':'success'},200)

# User logout functionality removes the token from the DB
@app.route('/api/logout',methods=['DELETE'])
def logout():
    token = AuthToken.query.filter_by(token=request.args['token']).first()

    #user.token.remove(token.auth_token)
    #db.session.delete(token)
    #db.session.commit()

    return response('', 200)


@app.route('/api/callback',methods=['POST'])
def callback():

    token_data = getUserToken(request.json['code'])
    userInfo = getUserInfo(token_data[0])

    # Check if it already exists in table
    user = User.query.filter_by(username=userInfo['id']).first()

    # Create a new uuid token
    userAuthToken = uuid.uuid4()

    auth = None

    if user is None:
        # Make a new user if user is not in table
        user = User(name=userInfo['display_name'],username=userInfo['id'],access_token=token_data[0],refresh_token=token_data[4],token_expiration=datetime.datetime.now()+datetime.timedelta(seconds=token_data[3]))
        db.session.add(user)
        db.session.commit()

    auth = AuthToken(user=user,token=userAuthToken,user_id=user.id)
    db.session.add(auth)
    db.session.commit()

    app.logger.info(f'{user.id}')

    if userInfo is None:
        abort(404)

    # Add the Auth token and refresh token to the database
    return response({'token':userAuthToken,'user_id':user.id},200)


def authenticate_user(req):

    token = AuthToken.query.filter_by(token=req.args['token']).first()

    if token is None:
        abort(401)

    user = token.user

    if user is None:
        abort(401)


    # refresh token if needed
    if (user.token_expiration <= datetime.datetime.now()):
        refresh_token(user)

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
        return f'{error.code}'


def response(json,code):
    response = jsonify(json)
    response.status_code = code
    return response


def refresh_token(user):
    token_data = refreshToken(user.refresh_token)
    user.access_token=token_data[0]
    user.refresh_token=token_data[4]
    user.token_expiration=datetime.datetime.now()+datetime.timedelta(seconds=token_data[3])
    db.commit()
