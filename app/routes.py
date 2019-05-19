from app import app, db
from app.models import User
from app.config import ERR_401, ERR_404

from flask import jsonify, request, abort, Response

@app.route('/')
def root():
    u = User(name="Winston")
    # db.session.add(u)
    # db.session.commit()

    return jsonify(u.to_dict())

# List playlists
@app.route('/api/playlists', methods=['GET'])
def list_playlists():

    user = authenticate_user(request)

    #TODO
    return None


# Edit playlist
@app.route('/api/playlists/:id',methods=['POST'])
def edit_playlist(request):

    user = authenticate_user(request)

    # TODO
    return None

# Playlist details
@app.route('/api/playlists/:id',methods=['GET'])
def get_playlist_details(request):

    user = authenticate_user(request)

    # TODO
    return None

# Create playlist
@app.route('/api/playlists/create',methods=['POST'])
def create_playlist(request):

    user = authenticate_user(request)

    # TODO
    return None

# Delete playlist
@app.route('/api/playlists/:id',methods=['DELETE'])
def delete_playlist(request):

    user = authenticate_user(request)

    # TODO
    return None

def authenticate_user(request):

    if 'token' not in request.form:
        abort(401)

    # get the username / user
    user = User(token=request.form['token'])

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
        return ERR_404
    if(error.code==401):
        return ERR_401
    else:
        return f'{error}'
