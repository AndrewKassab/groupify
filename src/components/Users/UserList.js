import React from 'react';
import GenericTable from '../common/GenericTable';

const keys = [
  {title: 'Name', key: 'name'},
  {title: 'Artists', key: 'artists'},
  {title: 'Length', key: 'duration'},
];

function UserList({ users }) {
  return <GenericTable items={users} keys={keys} name="Tracks" />;
}

export default TrackList;
