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

username1 = "djthomas619"
username2 = "123881475" 

token1 = ''
token2 = 'BQC4X3SNxem5DxvXdTksyP2DSmc8nGWJBaIbkR8ORiW4rjjGldHgUT3FSGtcLH7QHuCbAYoGBiX8MVFYwGm6fgC_YoodrWZsErnXwmEWz-S4nlqky7FJLXwiwuadsRh__0Q0N27j-MOZjonAc24O-L-9nNMm5jETK1WY_kOu7XLVr60lkJrxRfccC7aUhGlFEWIXyDMUozRjDsS528MlL_w1EzOcl5MLv_7Lkmrj3SjhxuLeWktmqA'

scope = 'user-read-recently-played user-top-read user-library-modify user-library-read playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative'

users = {}
users[username1] = []
users[username2] = []
test = createplaylist
test.create_playlist([username1,username2],[token1,token2],users, 3600000)
