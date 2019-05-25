class Artist:

    def __init__(self, artist_object):
        self.artist_id = id
        self.related_artists = []
        self.__retrieve_info(artist_object)

    # TODO: 
    def __retrieve_info(self, artist_object):
        pass
        self.artist_id = artist_object['id']
        # TODO: Retrieve related artists

    def is_related_artist(self, artist):
        for current_artist in self.related_artists:
          if current_artist.artist_id == artist.artist_id:
              return True
        return False