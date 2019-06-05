import Cookies from 'js-cookie';
import queryString from 'query-string';

const USER_ID = 'groupify-uid';

function tokenURL(path, params = {}) {
  return buildUrl(path, Object.assign(params, {token: getToken()}));
}

function buildUrl(url, parameters) {
  let qs = "";
  for (const key in parameters) {
      if (parameters.hasOwnProperty(key)) {
          const value = parameters[key];
          qs +=
              encodeURIComponent(key) + "=" + encodeURIComponent(value) + "&";
      }
  }
  if (qs.length > 0) {
      qs = qs.substring(0, qs.length - 1); //chop off last "&"
      url = url + "?" + qs;
  }

  return url;
}

function api(path) {
  return fetch(path, {
    accept: "application/json"
  })
    .then(checkStatus)
    .then(parseJSON);
}

function authReq(path, params = {}) {
  return api(tokenURL(path, params));
}

function postData(url = '', data = {}, auth = true, method = 'POST') {
  // Default options are marked with *

  return fetch(auth ? tokenURL(url) : url, {
    method: method,
    body: JSON.stringify(data),
    headers:{
      'Content-Type': 'application/json'
    }
  })
  .then(checkStatus)
  .then(parseJSON); // parses JSON response into native Javascript objects
}

function checkStatus(response) {
  if (response.status >= 200 && response.status < 300) {
    return response;
  }
  const error = new Error(`HTTP Error ${response.statusText}`);
  error.status = response.statusText;
  error.response = response;
  console.log(error); // eslint-disable-line no-console
  throw error;
}

function parseJSON(response) {
  return response.json();
}

function getToken() {
  return Cookies.get('token');
}

function setToken(token) {
  Cookies.set('token', token, { expires: 180 });
}

function login(query, history) {
  const spotifyArgs = queryString.parse(query);
  console.log(spotifyArgs);

  if (spotifyArgs['error']) {
    history.push("/");
  }

  postData('/api/callback', spotifyArgs, false)
  .then(res => {
    setToken(res.token);
    Cookies.set(USER_ID, res.user_id)
    history.push("/playlists");
  });
}

function logout() {
  postData('/api/logout', {}, true, 'DELETE').then(() => {
    Cookies.remove('token');
    window.location.reload(false);
  });
}

// Playlist methods
function createPlaylist(name, users, playlists, duration, userPlaylists, defaultAdd = false) {
  const dat = {
    name: name,
    duration: duration,
    users: users,
    playlists: playlists,
    userPlaylists: userPlaylists,
    defaultAdd: defaultAdd
  };

  return postData('/api/playlists/create', dat);
}

function editPlaylist(id, name) {
  return postData(`/api/playlists/${id}`, {name: name});
}

function addToSpotify(id) {
  return postData(`/api/playlists/${id}/spotify`);
}

function getPlaylist(id) {
  return authReq(`/api/playlists/${id}`);
}

function listPlaylists() {
  return authReq(`/api/playlists`);
}

// Search methods
function spotifyPlaylists(userId) {
  return authReq(`/api/search/playlists/${userId}`);
}

function listUsers() {
  return authReq('/api/search/users');
}

function loggedIn() {
  return !!getToken();
}

function userId() {
  return parseInt(Cookies.get(USER_ID));
}

const Client = {
  login,
  logout,

  listPlaylists,
  createPlaylist,
  editPlaylist,
  getPlaylist,

  addToSpotify,
  spotifyPlaylists,
  listUsers,

  loggedIn,
  userId,
};
export default Client;
