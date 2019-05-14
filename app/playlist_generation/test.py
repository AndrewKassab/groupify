from playlist_generation.objects.user import User
from playlist_generation.objects.track import Track
from playlist_generation.objects.artist import Artist
from playlist_generation.objects.primary_artist import PrimaryArtist 
from playlist_generation.objects.playlist import Playlist
from playlist_generation.factories.p_factory import PlaylistFactory

track_one = Track(1, None)
track_one.genre = 'electronic'
track_one.time_length = 3.5

track_two = Track(2, None)
track_two.genre = 'electronic'
track_two.time_length = 4.0

artist_one = PrimaryArtist( 1 )
artist_one.top_tracks = {track_one, track_two}

track_three = Track(3, None)
track_three.genre = 'hip-hop'
track_three.time_length = 3.0

track_four = Track(4, None)
track_four.genre = 'hip-hop'
track_four.time_length = 3.2

artist_two = PrimaryArtist( 2 )
artist_two.top_tracks = {track_three, track_four}

track_five = Track(3, None)
track_five.genre = 'electronic'
track_five.time_length = 3.0

track_six = Track(4, None)
track_six.genre = 'electronic'
track_six.time_length = 3.2

artist_three = Artist( 2 )
artist_three.top_tracks = {track_five, track_six}

artist_one.add_related_artist(artist_three)