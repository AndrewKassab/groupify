from app import app, db
from app.models import User
from spotify import *

from flask import jsonify, request, abort, Response

@app.route('/')
def root():
    u = User(name="Winston")
    # db.session.add(u)
    # db.session.commit()

    return jsonify(u.to_dict())

@app.route('/api/signup')
def signup():
    authorization_header = user_Authorization()


# List playlists
@app.route('/api/playlists', methods=['GET'])
def list_playlists():

    user = authenticate_user(request)

    #TODO
    # Get the playlists from the user

    return None


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

    response = jsonify({'playlist': {
        'id': group_id,
        'name': name,
        },
        'status': 'success'
    })

    response.status_code = 200

    return response

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


def authenticate_user(request):

    if 'token' not in request.form:
        abort(401)

    # get the username / user
    user = User.query.filter_by(token=request.form['token']).first()

    if user is None:
        abort(401)

    return user

@app.errorhandler(401)
def custom_401(error):
    return std_error_handler(error)

@app.errorhandler(404)
def custom_404(error):
    return std_error_handler(error)

def std_error_handler(error):
    response = jsonify({
        'message':f'{get_error_msg(error)}',
        'code':f'{error.code}',
        'status':'error'
    })

    response.status_code = error.code

    return response

def get_error_msg(error):
    if(error.code==404):
        return '404 MESSAGE'
    if(error.code==401):
        return '401 MESSAGE'
    else:
        return f'{error}'
