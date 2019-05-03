from abc import ABC, abstractmethod
import random

class PlaylistFactory(ABC):

    # List of songs as a final result of creation
    playlist = []

    # List users associtaed with this playlist
    users = []

    # The union list to be filtered
    unionList = []

    # The intersect list to be filtered
    intersectList = []

    # Set by user or generally set to a default length
    playlist_length = 0

    # Run from constructor add users
    @abstractmethod
    def create(self): pass

    # Lvl 1 filter
    @abstractmethod
    def filterIntersect(self): pass

    # Lvl 1 filter
    @abstractmethod
    def filterUnion(self): pass

    # Lvl 2 filter
    @abstractmethod
    def filterIntersectMostPlayed(self): pass

    # Lvl 2 filter
    @abstractmethod
    def filterUnionMostPlayed(self): pass

    # Lvl 3 filter
    @abstractmethod
    def filterUnionSimilarities(self): pass

    # Lvl 4 filter
    @abstractmethod
    def filterByLength(self): pass

    # Combine union list and intersect list
    def combine(self):
        # Convert both lists to sets
        unionSet = set(unionList)
        intersectSet = set(intersectList)

        # Merge the sets
        unionSet.union(intersectSet)

        # Finally convert to list
        playlist = list(unionSet)


    def getPlaylist():
        return playlist
