import React from 'react';
import { Table } from 'react-bootstrap';

function GenericTable({ items, keys, name }) {
  return (
    <Table hover size="sm">
      <thead>
        <tr>
          <th>#</th>
          {
            keys.map((key, index) => (
              <th key={`${name}-header-${index}`}>
                { key.title }
              </th>
            ))
          }
        </tr>
      </thead>
      <tbody>
        {
          items.map((item, index) => (
            <tr key={`${name}-${item.id}`}>
              <td>{ index + 1 }</td>
              { keys.map(key =>
                <td key={`${name}-${item.id}-${key.key}`}>
                  { key.fn ? key.fn(item[key.key]) : item[key.key] }
                </td>
              )}
            </tr>
          ))
        }
      </tbody>
    </Table>
  );
}

export default GenericTable;
