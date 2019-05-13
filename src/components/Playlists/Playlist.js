import React from 'react';
import { Col, Row, Alert } from 'react-bootstrap';
import {
  Link, Switch, Route, Redirect,
} from 'react-router-dom';
import PlaylistShow from './PlaylistShow';
import PlaylistCreate from './PlaylistCreate';
import PlaylistEdit from './PlaylistEdit';

function Playlist({ match, playlists }) {
  const playlist = playlists.find(plist => plist.id == match.params.id);

  if (match.params.id == 'create') {
    return <PlaylistCreate />;
  }

  if (!playlist) {
    return (
      <Alert variant="danger">
        No such playlist found!
        Return to all <Alert.Link as={Link} to="/playlists">playlists</Alert.Link>.
      </Alert>
    );
  }

  const show = (props => <PlaylistShow {...props} playlist={playlist} key={playlist.id} />);

  return (
    <Switch>
      <Route exact path={match.url} render={show} />
      <Redirect to={match.url} />
    </Switch>
  );
}

export default Playlist;
