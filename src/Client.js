import Cookies from 'js-cookie';

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

function postData(url = '', data = {}) {
  // Default options are marked with *
  const body = Object.assign({token: getToken()}, data);
  return fetch(url, {
    method: 'POST',
    body: JSON.stringify(body),
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
  Cookies.set('token', token);
}

function login(token) {
  setToken(token);
}

function logout() {
  Cookies.remove('token');
}

// Playlist methods
function createPlaylist(name, users, playlists, durantion) {
  return postData('/api/playlists/create', {
    name: name,
    duration: duration,
    users: users,
    playlists: playlists
  });
}

function editPlaylist(id, name) {
  return postData(`/api/playlists/${id}`, {name: name});
}

function getPlaylist(id) {
  return authReq(`/api/playlists/${id}`)
}

// Search methods
function spotifyPlaylists(userId) {
  return authReq(`/api/search/playlists/${userId}`);
}

function listUsers() {
  return authReq('/api/search/users');
}

const Client = {
  login,
  logout,

  createPlaylist,
  editPlaylist,
  getPlaylist,

  spotifyPlaylists,
  listUsers,

};
export default Client;
