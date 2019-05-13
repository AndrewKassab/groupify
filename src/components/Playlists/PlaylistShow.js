import React from 'react';
import { Link } from 'react-router-dom';
import TrackList from '../Tracks/TrackList';

function PlaylistShow({ playlist }) {
  return (
    <div>
      <h2>{ playlist.name }</h2>

      <TrackList tracks={playlist.tracks} />
    </div>
  );
}

export default PlaylistShow;
