First, run in terminal:

export SPOTIPY_CLIENT_ID='2832305d25ab48839092c9e11fd94f59'
export SPOTIPY_CLIENT_SECRET='214084c09b6e4369b0e72ba244c3d786'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'



Run file: with argv[1] being spotify username with one playlist.
Ex:
py start.py username

Outputs all unique artists and genres, works for a username with one playlist, not multiple.

Takes about 15-30 seconds, probably need a database for spotify songs beforehand. I use my username fatalis222


