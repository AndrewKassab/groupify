import React from 'react';
import TrackList from '../Tracks/TrackList';
import { Link } from 'react-router-dom';

function PlaylistShow({ playlist }) {
  return (
    <div>
      <h2>{ playlist.name }</h2>

      <TrackList tracks={playlist.tracks} />
    </div>
  );
}

export default PlaylistShow;
