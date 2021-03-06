import Cookies from 'js-cookie';
import queryString from 'query-string';

const USER_ID = 'groupify-uid';
const NAME = 'groupify-name';

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

function editPlaylist(id, attr) {
  return postData(`/api/playlists/${id}`, attr);
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

function userName() {
  return Cookies.get(NAME);
}

function whoAmI() {
  authReq('/api/me').then(res => {
    Cookies.set(USER_ID, res.user.id);
    Cookies.set(NAME, res.user.name);
  }).catch(e => {
    Cookies.remove('token');
  });
}

let previous;
let lastTimeout;
let callback;

const periodicCheck = () => {
  lastTimeout = setTimeout(periodicCheck, 5000);
  const id = lastTimeout;

  return authReq('/api/search/latest').then(latest => {
    if (previous === undefined) {
      previous = latest;
    } else if (id !== lastTimeout) {
      // Ensure we are the latest executing instance
      return;
    }

    if (JSON.stringify(latest) !== JSON.stringify(previous)) {
      console.log('Change detected!', previous, ' => ', latest);
      callback({previous, latest});
      previous = latest;
    }
  });
};

function startPoll(onChange) {
  stopPolling();
  callback = onChange;
  periodicCheck();
}

function manualPoll() {
  clearTimeout(lastTimeout);
  return periodicCheck();
}

function stopPolling() {
  clearTimeout(lastTimeout);
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
  userName,
  whoAmI,

  startPoll,
  manualPoll,
  stopPolling
};

export default Client;
export * from './helpers';
