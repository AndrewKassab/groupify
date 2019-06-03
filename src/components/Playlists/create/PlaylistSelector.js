import React from 'react';
import { Accordion, Card } from 'react-bootstrap';

import UserCard from './UserCard';

const PlaylistSelector = ({ update, values, playlists, users }) => {
  const handleChange = (user, playlists) => {
    console.log(user, playlists);
    // update(vals);
  }

  return (
    <>
      <h3>Select Playlists:</h3>
      <Accordion>
        { users.map((u) => <UserCard key={`ucard|u=${u.value}`} {...u} onChange={handleChange} />) }
        {
          users.length < 2 &&
          <Card><Card.Header>You must add another user</Card.Header></Card>
        }
      </Accordion>
    </>
  );
};

export default PlaylistSelector;
