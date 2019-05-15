from app import app, db
from app.models import User

from flask import jsonify

@app.route('/')
def root():
    u = User(name="Winston")
    # db.session.add(u)
    # db.session.commit()

    return jsonify(u.to_dict())

# List playlists
@app.route('/api/playlists', methods=['GET'])
def list_playlists(request):

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

@app.errorhandler(401)
def custom_401(error):
    return Response('<Bad Request user not found authenticated- flask_start.py>', 401, {''})


def authenticate_user(request):

    if 'auth_token' not in request:
        abort(401)

    # get the username / user
    user = None

    if user is None:
        abort(401)

    return user
