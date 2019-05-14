import spotipy

# Main function must call settings.__init__(token) before using other objects
def __init__(self, token)
    # Declare Spotify object for API calls in other files
    # Token has already been authorized
    
    global spotify
    spotify = spotipy.Spotify(auth=token)
