import React from 'react';
import { Col, Row, Alert } from 'react-bootstrap';
import PlaylistShow from './PlaylistShow';
import { Link, Switch, Route } from 'react-router-dom';

function Playlist({ match, playlists }) {
  let playlist = playlists.find((plist) =>
    plist.id == match.params.id
  );

  if (match.params.id == 'create') {
    return <PlaylistCreate />;
  }

  if (!playlist) {
    return (
      <Alert variant='danger'>
        No such playlist found!
        Return to all <Alert.Link as={Link} to='/playlists'>playlists</Alert.Link>.
      </Alert>
    );
  }

  const show = (props => <PlaylistShow {...props} playlist={playlist} />);
  const edit = (props => <PlaylistEdit {...props} playlist={playlist} />);

  return (
    <Switch>
      <Route path={`${match.url}/edit`} render={edit} />
      <Route render={show} />
    </Switch>
  );
}

export default Playlist;
