import React from 'react';
import { Accordion, Card } from 'react-bootstrap';

import UserCard from './UserCard';

const PlaylistSelector = ({ update, values, data }) => {

  const cards = data.map(
    ({uid, label, playlists}) =>
    <UserCard key={`ucard|u=${uid}`} uid={uid} label={label} onChange={update} />
  );

  return (
    <>
      <h3>Select Playlists:</h3>
      <Accordion>
        { cards }
        {
          users.length < 2 &&
          <Card><Card.Header>You must add another user</Card.Header></Card>
        }
      </Accordion>
    </>
  );
};

export default PlaylistSelector;
