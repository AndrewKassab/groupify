import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { ListGroup, Form, FormControl } from 'react-bootstrap';

import { withStore } from '@spyna/react-store';

function PlaylistList({ playlists }) {
  const [search, setSearch] = useState('');

  const handleSearch = e => setSearch(e.target.value.toLowerCase());

  return (
    <div>
      <h3>Playlists:</h3>

      <Form className="mb-3">
        <FormControl type="text" placeholder="Search" onChange={handleSearch} />
      </Form>

      <ListGroup variant="flush">
        {
          playlists.filter(p => p.name.toLowerCase().includes(search)).map(playlist => (
            <ListGroup.Item action as={NavLink} key={`plist-${playlist.id}`} to={`/playlists/${playlist.id}`}>
              { playlist.name }
            </ListGroup.Item>
          ))
        }
      </ListGroup>
    </div>
  );
}

export default withStore(PlaylistList, ['playlists']);
