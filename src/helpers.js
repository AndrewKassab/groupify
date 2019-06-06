const findPlaylist = (pid, playlists) => playlists.find(plist => plist.id === pid);

const modifyPlaylist = (id, store, func) => {
  let playlists = store.get('playlists');
  let plist = findPlaylist(id, playlists);
  func(plist);
  store.set('playlists', playlists);
};

export { findPlaylist, modifyPlaylist };
