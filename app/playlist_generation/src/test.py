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


scope = 'user-top-read'
#username1 = "groupiftytest1@googlemail.com"
username1 = "iyv4pmv1nry9uztvq60z46i7f"
#fatalis workout id 1lzlp5PJ81Wjy80nCjp0aN
playlistid1 = "6D7KieZcqooniV9W9cuBPw"

#username2 = "groupiftytest1@gmail.com"
username2 = "62xvmx1yt7f57jxa0jgjs6qg0"
playlistid2 = "37i9dQZF1DX0XUsuxWHRQd"
#username1 = sys.argv[1]


try:
    token1 = util.prompt_for_user_token(username1,scope)
except:
    os.remove(f".cache-{username1}")
    token1 = util.prompt_for_user_token(username1,scope)

try:
    token2 = util.prompt_for_user_token(username2,scope)
except:
    os.remove(f".cache-{username2}")
    token2 = util.prompt_for_user_token(username2,scope)


users = {}
users[username1] = playlistid1
users[username2] = playlistid2
test = createplaylist
test.create_playlist([username1,username2],[token1,token2],users, 30)



#########################################
# playlists = user1.playlists
# for i in playlists:
#     print("-------------------------------------------------------------------------------------")
#     print("Id:"+ i.id + "   " + "Name:" + "  Time Length:" , i.duration)
#     for j,k in i.tracks.items():
#         print("Id:" + k.song_id+ "\nTitle:" + k.name + "\nArtist name:" + " Duration:" , k.duration , "ms")
#         print()
#     print()




#
# track_one = Track(1, None)
# track_one.genre = 'electronic'
# track_one.time_length = 3.5
#
# track_two = Track(2, None)
# track_two.genre = 'electronic'
# track_two.time_length = 4.0
#
# #artist_one = PrimaryArtist( 1 )
# #artist_one.top_tracks = {track_one, track_two}
#
# track_three = Track(3, None)
# track_three.genre = 'hip-hop'
# track_three.time_length = 3.0
#
# track_four = Track(4, None)
# track_four.genre = 'hip-hop'
# track_four.time_length = 3.2
#
# #artist_two = PrimaryArtist( 2 )
# #artist_two.top_tracks = {track_three, track_four}
#
# track_five = Track(3, None)
# track_five.genre = 'electronic'
# track_five.time_length = 3.0
#
# track_six = Track(4, None)
# track_six.genre = 'electronic'
# track_six.time_length = 3.2
#
# artist_three = Artist( 2 )
#artist_three.top_tracks = {track_five, track_six}

#artist_one.add_related_artist(artist_three)
