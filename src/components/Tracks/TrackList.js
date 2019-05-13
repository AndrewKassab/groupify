import React from 'react';
import { Table } from 'react-bootstrap';


function TrackList({ tracks }) {
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Artists</th>
        </tr>
      </thead>
      <tbody>
        {
          tracks.map((track, index) =>
            <tr key={`track-${track.id}`}>
              <td>{ index + 1 }</td>
              <td>{ track.name }</td>
              <td>__artists__</td>
            </tr>
          )
        }
      </tbody>
    </Table>
  );
}

export default TrackList;
