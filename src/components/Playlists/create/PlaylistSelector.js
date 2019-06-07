import React from 'react';
import { Accordion, Card } from 'react-bootstrap';

import UserCard from './UserCard';

const PlaylistSelector = ({ update, data }) => {

  const cards = data.map(
    ({uid, label, playlists}) =>
    <UserCard key={`ucard|u=${uid}`} uid={uid} label={label} onChange={update} playlists={playlists} />
  );

  return (
    <>
      <h3>Select Playlists: <span className="text-muted h5">(optional)</span></h3>
      <Accordion>
        { cards }
        {
          cards.length < 2 &&
          <Card><Card.Header>You must add another user</Card.Header></Card>
        }
      </Accordion>
    </>
  );
};

export default PlaylistSelector;
