// import { Playlist } from './Playlist';
import React from 'react';
import { NavLink } from 'react-router-dom';
import { ListGroup, Form, FormControl } from 'react-bootstrap';

function PlaylistList({ playlists }) {
  return (
    <div>
      <h3>Playlists:</h3>

      <Form className="mb-3">
        <FormControl type="text" placeholder="Search" />
      </Form>

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
