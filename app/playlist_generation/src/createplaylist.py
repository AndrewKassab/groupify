from user import User
from p_factory import PlaylistFactory

# user_playlist_ids is a dictionary of ids, where the keys are the usernames so 
# there is a list of desired playlist ids to pull from for each specific user at 
# their key. 

def create_playlist(usernames, user_playlist_ids, desired_length):
  users = []
  for username in usernames:
    users.append(User(username, user_playlist_ids[username]))

  my_factory = PlaylistFactory(users, desired_length)

  # ths means that usernames[0] needs to have the main groupify user 
  my_factory.create(users[0])



# TODO: 
# call create_playlist() with appropriate arguments
