# This is an interface for inheriting classes that 
# defines the proccess for which a playlist should 
# be generated by the groupify app. 

from abc import ABC, abstractmethod
import random

class PlaylistFactory(ABC):

    # playlist object 
    playlist = none

    # List of songs as a final result of creation
    songs = []

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
        songs = list(unionSet)

        # TODO: 
        # playlistName = Groupify-DATE
        # playlistImage = groupify album art by default (?) 

        playlist = playlist( songs, playlistName, playlistImage )


    def getPlaylist():
        return playlist
