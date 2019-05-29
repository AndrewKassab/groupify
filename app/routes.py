from app import app, db
from app.models import User
from app.spotify import *

from flask import jsonify, request, abort, Response, redirect

@app.route('/')
def root():
    u = User(name="Winston")
    # db.session.add(u)
    # db.session.commit()

    return jsonify(u.to_dict())

@app.route('/api/signup')
def signup():
    response = getUser()

    return redirect(response)

# List playlists
@app.route('/api/playlists', methods=['GET'])
def list_playlists():

    user = authenticate_user(request)

    # The list of playlists to eventually be returned
    playlists = []

    # Iterate through all of the user's groups
    for group in user.groups:

        playlists.append({'id': group.id, 'name': group.title, 'state':'done'})

    response = jsonify()
    response.status_code = 200

    return response({'playlists': playlists, 'status':'success'},200)


# Edit playlist
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


    return None

# Create playlist
@app.route('/api/playlists/create',methods=['POST'])
def create_playlist():

    user = authenticate_user(request)

    # TODO
    return None

# Delete playlist
@app.route('/api/playlists/<int:group_id>',methods=['DELETE'])
def delete_playlist(group_id):

    user = authenticate_user(request)

    # TODO
    return None

@app.route('/api/logout',methods=['DELETE'])
def logout():

    user = authenticate_user(request)


    return None


@app.route('/callback/')
def callback():

    if request.args['code'] is None:
        #return redirect('http://localhost:3000')

    token_data = getUserToken(request.args['code'])
    userInfo = getUserInfo()

    print(token_data)

    # Add the Auth token and refresh token to the database
    user = User(name=userInfo['display_name'],username=userInfo['id'],access_token=token_data[0],refresh_token=token_data[1],token_expiration=token_data[3])

    print(userInfo)
    if userInfo is None:
        abort(404)

    return redirect('http://localhost:3000')


def authenticate_user(request):

    if 'token' not in request.form:
        abort(401)

    token = AuthToken.query.filter_by(token=request.form['token']).first()
    user = token.user

    if user is None:
        abort(401)

    # refresh token if needed
    if user.token_expiration >= now:
        token_data = refreshToken(3600)
        user.access_token=token_data[0]
        user.refresh_token=token_data[1]
        user.token_expiration=token_data[3]
        deb.commit()

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
