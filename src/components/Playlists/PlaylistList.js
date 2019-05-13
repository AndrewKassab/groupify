// import { Playlist } from './Playlist';
import React from 'react';
import { NavLink } from 'react-router-dom';
import { ListGroup } from 'react-bootstrap';

function PlaylistList({ playlists }) {
  console.log(playlists);
  return (
    <div>
      <h3>Playlists:</h3>

      <ListGroup variant="flush">
        {
          playlists.map(playlist => (
            <ListGroup.Item action activeClassName="active" as={NavLink} key={`plist-${playlist.id}`} to={`/playlists/${playlist.id}`}>
              { playlist.name }
            </ListGroup.Item>
          ))
        }
      </ListGroup>
    </div>
  );
}

export default PlaylistList;
