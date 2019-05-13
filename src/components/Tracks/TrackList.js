import React from 'react';
import { Table } from 'react-bootstrap';

function TrackList({ tracks }) {
  return (
    <div className="pt-3">
      <h4>Tracks:</h4>

      <Table hover size="sm">
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Artists</th>
            <th>Length</th>
          </tr>
        </thead>
        <tbody>
          {
            tracks.map((track, index) =>
              <tr key={`track-${track.id}`}>
                <td>{ index + 1 }</td>
                <td>{ track.name }</td>
                <td>{ track.artists }</td>
                <td>{ track.duration }</td>
              </tr>
            )
          }
        </tbody>
      </Table>
    </div>
  );
}

export default TrackList;
