const users = [
  {id: 1, name: "Winston", username: "r167"},
  {id: 2, name: "Sowrya", username: "sowrya-da-man"},
  {id: 3, name: "Steven", username: "ya-boi-steven"},
  {id: 4, name: "Alex", username: "Its-justalex"},
  {id: 5, name: "Joyce", username: "hello"}
];

const spotifyPlaylists = {
  1: [
    {name: "playlist 1", id: "blah1"},
    {name: "playlist 2", id: "blah2"},
    {name: "playlist 3", id: "blah3"}
  ],
  2: [
    {name: "playlist 1", id: "blah4"},
    {name: "playlist 2", id: "blah5"},
    {name: "playlist 3", id: "blah6"}
  ],
};

const usersById = (ids) => users.filter(({ id }) => ids.includes(id));

const playlists = [
  {
    id: 1,
    name: 'Hello world',
    tracks: [
      {
        id: 1, name: 'blah', artists: 'artist', duration: 94,
      },
      {
        id: 2, name: 'blah2', artists: 'artist', duration: 255,
      },
    ],
    users: usersById([1, 3, 5]),
  },
  {
    id: 2,
    name: 'Other playlist',
    tracks: [
      {
        id: 3, name: 'other', artists: 'artist', duration: 150,
      },
      {
        id: 4, name: 'other song', artists: 'artist1 & artist2', duration: 78,
      },
    ],
    users: usersById([2, 4, 5]),
  },
];

module.exports = {
  playlists: playlists,

  users: users,
  userOptions: users.map((u) => {return {value: u.id, label: `${u.name} - ${u.username}`}}),

  spotifyPlaylists: spotifyPlaylists,
};
