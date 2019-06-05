import React from 'react';
import { Col, Row, Alert, Spinner } from 'react-bootstrap';
import {
  Link, Switch, Route, Redirect,
} from 'react-router-dom';
import PlaylistShow from './PlaylistShow';

import { withStore } from '@spyna/react-store';
import Client from '../../Client';

const findPlaylist = (pid, playlists) => playlists.find(plist => plist.id === pid);

const modifyPlaylist = (id, store, func) => {
  let playlists = store.get('playlists');
  let plist = findPlaylist(id, playlists);
  func(plist);
  store.set('playlists', playlists);
}

function Playlist({ match, playlists, store }) {
  const pid = parseInt(match.params.id);
  const playlist = findPlaylist(pid, playlists);

  if (store.get('playlist.active') !== pid) {
    store.set('playlist.active', pid);
  }

  if (!playlist) {
    return (
      <Alert variant="danger">
        No such playlist found!
        Return to all <Alert.Link as={Link} to="/playlists">playlists</Alert.Link>.
      </Alert>
    );
  }

  const rename = name => {
    const id = playlist.id;
    Client.editPlaylist(id, {name: name}).then(res => {
      modifyPlaylist(id, store, p => {
        p.name = res.playlist.name;
        p.details.name = res.playlist.name;
      })
    });
  }

  const changeVisibility = state => {
    const id = playlist.id;
    Client.editPlaylist(id, {visible: state}).then(res => {
      modifyPlaylist(id, store, p => {
        p.visible = res.playlist.visible;
        p.details.visible = res.playlist.visible;
      })
    });
  }

  let show;
  if (playlist.cached) {
    show = (props => <PlaylistShow {...props} playlist={playlist.details} key={playlist.id} rename={rename} changeVisibility={changeVisibility} />);
  } else {
    show = () => <Spinner animation="border" />;
    Client.getPlaylist(pid).then(res => {
      modifyPlaylist(pid, store, p => {
        p.details = res.playlist;
        p.cached = true;
      });
    });
  }

  return (
    <Switch>
      <Route exact path={match.url} render={show} />
      <Redirect to={match.url} />
    </Switch>
  );
}

export default withStore(Playlist, ['playlists']);
