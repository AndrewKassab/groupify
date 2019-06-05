import React, { useState } from 'react';
import { NavLink, withRouter } from 'react-router-dom';
import { ListGroup, Form, FormControl } from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import { withStore } from '@spyna/react-store';

const PlaylistItem = ({playlist}) => (
  <ListGroup.Item action as={NavLink} to={`/playlists/${playlist.id}`}>
    <div className="d-flex">
      <div className="w-100">{ playlist.name }</div>
      { playlist.visible || <div className="pl-1 flex-shrink-1 align-self-center"><FontAwesomeIcon icon="eye-slash"/></div> }
    </div>
  </ListGroup.Item>
);

function PlaylistList({ playlists, store }) {
  const [search, setSearch] = useState('');
  const [focus, setFocus] = useState(false);

  const active = store.get('playlist.active');

  const handleSearch = e => setSearch(e.target.value.toLowerCase());
  const filterOrId = func => p => (p.id === active || func(p));
  const filteredResults = () => {
    if (focus) {
      return playlists.filter(filterOrId(p => p.name.toLowerCase().includes(search))).map(playlist => (
        <PlaylistItem playlist={playlist} key={`plist-${playlist.id}`} />
      ));
    } else {
      return playlists.filter(filterOrId(p => p.visible)).map(playlist => (
        <PlaylistItem playlist={playlist} key={`plist-${playlist.id}`} />
      ));
    }
  };

  return (
    <div>
      <h3>Playlists:</h3>

      <Form className="mb-3">
        <FormControl
          type="text"
          placeholder="Search"
          onChange={handleSearch}
          onFocus={() => setFocus(true)}
          onBlur={() => setTimeout(() => setFocus(search !== ""), 100)}
        />
      </Form>

      <ListGroup variant="flush">
        { filteredResults() }
      </ListGroup>
    </div>
  );
}

export default withRouter(withStore(PlaylistList, ['playlists']));
