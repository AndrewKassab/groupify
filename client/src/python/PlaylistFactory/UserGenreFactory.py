from PlaylistFactory import PlaylistFactory

class UserGenreFactory(PlaylistFactory):

    def __init__(self):
        return None

    # Run from constructor add users
    def create(self):
        return None

    # Lvl 1 filter
    def filterIntersect(self):
        return None

    # Lvl 1 filter
    def filterUnion(self):
        return None

    # Lvl 2 filter
    def filterIntersectMostPlayed(self):
        return None

    # Lvl 2 filter
    def filterUnionMostPlayed(self):
        return None

    # Lvl 3 filter
    def filterUnionSimilarities(self):
        return None

    # Lvl 4 filter
    def filterByLength(self):
        return None
