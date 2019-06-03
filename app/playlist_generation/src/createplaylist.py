from user import User
from p_factory import PlaylistFactory

def create_playlist(name, usernames, tokens, user_playlist_ids, desired_length):
  if len(usernames) != len(tokens):
    return None

  users = []
  for username, token in zip(usernames, tokens):
    users.append(User(username, token, user_playlist_ids[username]))

  my_factory = PlaylistFactory(name, users, desired_length)

  # NOTE:
  # ths means that usernames[0] needs to have the main groupify user
  # who is creating the playlist in the firstplace
  my_factory.create(users[0])
  
  return my_factory.get_track_objects()

  # TODO: Have each other user follow the newly created playlist
