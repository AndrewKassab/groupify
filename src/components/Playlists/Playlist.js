import React from 'react';
import { Col, Row, Alert } from 'react-bootstrap';
import TrackList from '../Tracks/TrackList';
import { Link } from 'react-router-dom';

function Playlist({ match, playlists }) {
  console.log(match.params.id);

  let playlist = playlists.find((plist) =>
    plist.id == match.params.id
  );

  if (!playlist) {
    return (
      <Alert variant='danger'>
        No such playlist found!
        Return to all <Alert.Link as={Link} to='/playlists'>playlists</Alert.Link>.
      </Alert>
    );
  }

  return (
    <div>
      <h2>{ playlist.name }</h2>

      <TrackList tracks={playlist.tracks} />
    </div>
  );
}

export default Playlist;
