import React from 'react';
import { Col, Row, Alert } from 'react-bootstrap';
import {
  Link, Switch, Route, Redirect,
} from 'react-router-dom';
import PlaylistShow from './PlaylistShow';

import { withStore } from '@spyna/react-store';
import Client from '../../Client';

const findPlaylist = (pid, playlists) => playlists.find(plist => plist.id === pid);

function Playlist({ match, playlists, store }) {
  const playlist = findPlaylist(match.params.id, playlists);

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
    Client.editPlaylist(id, name).then(() => {
      let playlists = store.get('playlists');
      let plist = findPlaylist(id, playlists);
      plist.name = name;
      store.set('playlists', playlists);
    });
  }

  const show = (props => <PlaylistShow {...props} playlist={playlist} key={playlist.id} onChange={rename} />);

  return (
    <Switch>
      <Route exact path={match.url} render={show} />
      <Redirect to={match.url} />
    </Switch>
  );
}

export default withStore(Playlist, ['playlists']);
