class Track:

    def __init__(self, id, name, artists, duration):
        self.id = id 
        self.name = name
        self.artists = artists
        self.duration = duration
        self.amt_saved = 1

    def increment_amt_saved(self):
        self.amt_saved += 1
