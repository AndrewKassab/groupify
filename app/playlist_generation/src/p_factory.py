import random
import sys
import copy
from user import User
sys.path.append("../")

class PlaylistFactory():

    def __init__(self, users, desired_length):
        self.users = users
        self.desired_length = desired_length * 1.25
        self.current_length = 0
        self.tracks = {}

    # Creates the playlist by running appropriate methods to filter songs
    def __create(self):
        self.__determine_track_list()
        self.__filter_length()
        return self.tracks
        
    # filters tracks into the final group based on percentage 
    def __determine_track_list(self):
        all_tracks = {}
    
    def __filter_length(self):
        pass