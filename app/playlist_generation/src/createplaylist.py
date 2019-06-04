from app.playlist_generation.src.user import user
from app.playlist_generation.src.p_factory import PlaylistFactory

def create_playlist(name, usernames, tokens, user_playlist_ids, desired_length):
  if len(usernames) != len(tokens):
    return None

  users = []
  for username, token in zip(usernames, tokens):
    users.append(user(username, token, user_playlist_ids[username]))

  my_factory = PlaylistFactory(name, users, desired_length)

  # Create the playlist on main user's account
  my_factory.create(users[0])

  return my_factory.get_track_objects()

