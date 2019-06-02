import React from 'react';
import GenericTable from '../common/GenericTable';

const keys = [
  {title: 'Name', key: 'name'},
  {title: 'Username', key: 'username'},
];

function UserList({ users }) {
  return <GenericTable items={users} keys={keys} name="Tracks" />;
}

export default UserList;
