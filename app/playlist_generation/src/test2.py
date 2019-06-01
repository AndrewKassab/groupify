#Added
#####################
import sys
sys.path.append('../')
#####################

from p_factory import PlaylistFactory
from user import User
from track import Track
import spotipy
import spotipy.util as util
import os

#Added
import createplaylist

#username1 = "groupiftytest1@googlemail.com"
username1 = "iyv4pmv1nry9uztvq60z46i7f"
playlistid1 = "37i9dQZF1DXdfhOsjRMISB" #Country

#username2 = "groupiftytest1@gmail.com"
username2 = "62xvmx1yt7f57jxa0jgjs6qg0"
playlistid2 = "37i9dQZF1DX0XUsuxWHRQd"
#username1 = sys.argv[1]

username3 = "sjlxndd19gvhkpk2canjveuuv" #groupifytest2@googlemail.com
playlistid3 = "3zR7RJEfXFjTANGXq53OiV" #on repeat 3zR7RJEfXFjTANGXq53OiV
                                       #pop drive 37i9dQZF1DWSThc8QnzIme

username4 = "b1yk8s40u2aorbujemv27dnmv"
playlistid4 = "37i9dQZF1DWXXQuxfjYVxb" #this is cardi b
# favorite music 0sxksn4wYGtb4RSfRYpAEf
#this is migos 37i9dQZF1DWUHuWFjknUw4


username5= "groupifytest3@googlemail.com"
username6 = "groupifytest3@gmail.com"
playlistid6 = "37i9dQZF1DX0XUsuxWHRQd"
username7 = "fatalis222"
playlistid7 = "1lzlp5PJ81Wjy80nCjp0aN"


scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'
token1 = util.prompt_for_user_token(username1, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')
token2 = util.prompt_for_user_token(username2, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')
token3 = util.prompt_for_user_token(username3, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')
token4 = util.prompt_for_user_token(username3, scope, client_id='7d2739378e2a47d8bc6cc89c63c5c4b0', client_secret='5d2535acb98847c5b166fadaee4fe436',redirect_uri='http://localhost:8888/callback/')


users = {}
users[username1] = playlistid1
users[username2] = playlistid2
users[username3] = playlistid3
users[username4] = playlistid4
test = createplaylist
test.create_playlist([username1,username4],[token1,token4],users, 500000)
