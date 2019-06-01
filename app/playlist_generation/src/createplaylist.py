from user import User
from p_factory import PlaylistFactory

# NOTE:
# user_playlist_ids is a dictionary of ids, where the keys are the usernames so
# there is a list of desired playlist ids to pull from for each specific user at
# their key.


def create_playlist(usernames, tokens, user_playlist_ids, desired_length):
  if len(usernames) != len(tokens):
    print("ERROR: Number of usernames does not match number of tokens")
  users = []
  for username, token in zip(usernames, tokens):
    users.append(User(username, token, [user_playlist_ids[username]]))

  my_factory = PlaylistFactory(users, desired_length)

  # NOTE:
  # ths means that usernames[0] needs to have the main groupify user
  # who is creating the playlist in the firstplace
  my_factory.create(users[0])


# TODO:
# call create_playlist() with appropriate arguments
