import React, { useState } from 'react';
import { NavLink, withRouter } from 'react-router-dom';
import { ListGroup, Form, FormControl, Button, InputGroup } from 'react-bootstrap';

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

function PlaylistList({ playlists, location }) {
  const [search, setSearch] = useState('');
  const [focus, setFocus] = useState(false);
  const [showHidden, setShowHidden] = useState(true);
  const [owner, setOwner] = useState(false);

  const clearSearch = () => {
    setFocus(false);
    setSearch('');
    setShowHidden(true);
    setOwner(false);
  };

  const active = parseInt(location.pathname.split('/').slice(-1));

  const handleSearch = e => setSearch(e.target.value.toLowerCase());
  const filterOrId = func => p => (p.id === active || func(p));

  const searchFilter = p => (
    (!owner || p.owner) &&
    (showHidden || p.visible) &&
    (p.name.toLowerCase().includes(search))
  );

  const filteredResults = () => {
    if (focus) {
      return playlists.filter(filterOrId(searchFilter)).map(playlist => (
        <PlaylistItem playlist={playlist} key={`plist-${playlist.id}`} />
      ));
    } else {
      return playlists.filter(filterOrId(p => p.visible)).map(playlist => (
        <PlaylistItem playlist={playlist} key={`plist-${playlist.id}`} />
      ));
    }
  };
  const showClear = () => {
    if (focus) {
      return (
        <InputGroup.Append>
          <Button variant="outline-secondary" onClick={clearSearch}>Clear</Button>
        </InputGroup.Append>
      );
    }
  }

  const showFilters = () => {
    if (focus) {
      return (
        <div>
          <Form.Check inline type="checkbox" label="Hidden" onChange={e => setShowHidden(e.target.checked)} checked={showHidden} />
          <Form.Check inline type="checkbox" label="Mine Only" onChange={e => setOwner(e.target.checked)} checked={owner} />
        </div>
      );
    }
  }

  return (
    <div>
      <h3>Playlists:</h3>

      <InputGroup className="mb-3">
        <FormControl
          type="text"
          placeholder="Search"
          onChange={handleSearch}
          onFocus={() => setFocus(true)}
        />
        { showClear() }
      </InputGroup>
      { showFilters() }

      <ListGroup variant="flush">
        { filteredResults() }
      </ListGroup>
    </div>
  );
}

export default withRouter(withStore(PlaylistList, ['playlists']));
