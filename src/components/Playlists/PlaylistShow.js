import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TrackList from '../Tracks/TrackList';
import UserList from '../Users/UserList';
import { Button, ButtonToolbar, InputGroup, FormControl, Dropdown, Tabs, Tab } from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

function PlaylistShow({ playlist, rename }) {

  const [name, setName] = useState(playlist.name);
  const [editName, setEditName] = useState(name);
  const [editMode, setEditMode] = useState(false);

  const saveName = () => {
    setName(editName);
    setEditMode(false);
    rename(editName);
  };

  const editor = (
    <InputGroup className="mb-2">
      <FormControl
        defaultValue={name}
        onChange={e => setEditName(e.target.value)}
      />
      <InputGroup.Append>
        <Button variant="outline-primary" onClick={saveName}>Save</Button>
        <Button variant="outline-secondary" onClick={() => setEditMode(false)}>Cancel</Button>
      </InputGroup.Append>
    </InputGroup>
  );

  const handleToggle = () => {
    console.log("TOGGLE");
  };

  const display = (
    <ButtonToolbar className="d-flex justify-content-between">
      <h2>{ name }</h2>
      <Dropdown alignRight>
        <Dropdown.Toggle variant="link" id="dropdown-basic">
          <span className="fa-layers fa-fw">
            <FontAwesomeIcon icon="circle" size="2x" />
            <FontAwesomeIcon icon="ellipsis-v" size="2x" inverse transform="shrink-6 right-3" />
          </span>
        </Dropdown.Toggle>

        <Dropdown.Menu>
          <Dropdown.Item onClick={() => setEditMode(true)}>Change Name</Dropdown.Item>
          <Dropdown.Item>Add to Spotify</Dropdown.Item>
          {/* <Dropdown.Divider />
          <Dropdown.Item onClick={handleToggle}>Hide Playlist</Dropdown.Item> */}
        </Dropdown.Menu>
      </Dropdown>
    </ButtonToolbar>
  );

  return (
    <div>
      { editMode ? editor : display }

      <Tabs defaultActiveKey="tracks" id="uncontrolled-tab-example">
        <Tab eventKey="tracks" title="Tracks">
          <TrackList tracks={playlist.tracks} />
        </Tab>
        <Tab eventKey="users" title="Users">
          <UserList users={playlist.users} />
        </Tab>
      </Tabs>
    </div>
  );
}

export default PlaylistShow;
