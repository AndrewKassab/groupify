import React from 'react';
import GenericTable from '../common/GenericTable';
import moment from 'moment';

const duration = dur => {
  const t = moment.utc(moment.duration(dur, 'seconds').asMilliseconds());
  return t.format('m:ss');
};

const keys = [
  {title: 'Name', key: 'name'},
  {title: 'Artists', key: 'artists'},
  {title: 'Length', key: 'duration', fn: duration},
];

function TrackList({ tracks }) {
  return <GenericTable items={tracks} keys={keys} name="Tracks" />;
}

export default TrackList;
