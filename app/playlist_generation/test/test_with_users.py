import spotipy
import spotipy.util as util
import os

#Added
import createplaylist

username1 = ""
username2 = "" 

token1 = ''
token2 = ''
scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'

users = {}
users[username1] = []
users[username2] = []
test = createplaylist
test.create_playlist([username1,username2],[token1,token2],users, 3600000)
