import React from 'react';
import { Form } from 'react-bootstrap';
import moment from 'moment';

const wrapChange = h => e => h(e.target.value);

const formatTime = (duration) => {
  let d = moment.duration(duration, 'minutes');

  return `${d.hours()}h ${d.minutes()}m`;
};

const PlaylistParams = ({updateName, updateDuration, name, duration}) => {
  return (
    <Form>
      <Form.Group controlId="playlistName">
        <Form.Label><h3>Playlist Name</h3></Form.Label>
        <Form.Control type="text" placeholder="Enter playlist name" value={name} onChange={wrapChange(updateName)} />
        {/* <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text> */}
      </Form.Group>

      <Form.Group controlId="playlistDuration">
        <Form.Label><h3>Target Duration: {formatTime(duration)}</h3></Form.Label>
        <Form.Control type="range" defaultValue={duration} onChange={wrapChange(updateDuration)} min="15" max="300" />
      </Form.Group>
    </Form>
  );
};

export default PlaylistParams;
