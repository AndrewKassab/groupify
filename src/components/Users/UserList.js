import React from 'react';
import GenericTable from '../common/GenericTable';

const owner = <span className="text-muted">Owner</span>;
const keys = [
  {title: 'Name', key: 'name'},
  {title: 'Username', key: 'username'},
  {title: 'Owner', key: 'owner', fn: b => b && owner }
];

function UserList({ users }) {
  return <GenericTable items={users} keys={keys} name="Tracks" />;
}

export default UserList;
