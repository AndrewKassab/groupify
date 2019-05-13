import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TrackList from '../Tracks/TrackList';
import { Button, ButtonToolbar, InputGroup, FormControl } from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

function PlaylistShow({ playlist }) {

  const [name, setName] = useState(playlist.name);
  const [editName, setEditName] = useState(name);
  const [editMode, setEditMode] = useState(false);

  let editor = (
    <InputGroup>
      <FormControl
        defaultValue={name}
      />
      <InputGroup.Append>
        <Button variant="outline-secondary">Save</Button>
        <Button variant="outline-secondary" onClick={() => setEditMode(false)}>Cancel</Button>
      </InputGroup.Append>
    </InputGroup>
  );

  let display = (
    <ButtonToolbar className="d-flex justify-content-between">
      <h2>{ name }</h2>
      <div>
        <Button className="mr-1" variant="outline-secondary" onClick={() => setEditMode(true)}>Change Name</Button>

        <Button className="mr-1" variant="outline-primary">Add to Spotify</Button>
        <Button variant="outline-danger">DELETE</Button>

        {/* <FontAwesomeIcon icon="ellipsis-v" /> */}
      </div>
    </ButtonToolbar>
  );

  return (
    <div>
      { editMode ? editor : display }

      <TrackList tracks={playlist.tracks} />
    </div>
  );
}

export default PlaylistShow;
