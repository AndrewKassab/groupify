import React from 'react';
import { Col, Row, Alert, Spinner } from 'react-bootstrap';
import {
  Link, Switch, Route, Redirect,
} from 'react-router-dom';
import PlaylistShow from './PlaylistShow';

import { withStore } from '@spyna/react-store';
import Client, { findPlaylist, modifyPlaylist } from '../../Client';

function Playlist({ match, playlists, store, history }) {
  const pid = parseInt(match.params.id);
  const playlist = findPlaylist(pid, playlists);

  if (!playlist) {
    return (
      <Alert variant="danger">
        No such playlist found!
        Return to all <Alert.Link as={Link} to="/playlists">playlists</Alert.Link>.
      </Alert>
    );
  }

  const rename = name => {
    const id = playlist.id;
    Client.editPlaylist(id, {name: name}).then(res => {
      modifyPlaylist(id, store, p => {
        p.name = res.playlist.name;
        p.details.name = res.playlist.name;
      });
    });
  }

  const addToSpotify = id => {
    Client.addToSpotify(id).then(res => {
      modifyPlaylist(id, store, p => {
        p.details.spotify_id = res.spotify_id;
      });
    });
  };

  const changeVisibility = visible => {
    const id = playlist.id;
    Client.editPlaylist(id, {visible: visible}).then(res => {
      modifyPlaylist(id, store, p => {
        p.visible = res.playlist.visible;
        p.details.visible = res.playlist.visible;
      });

      if (!res.playlist.visible) {
        history.push('/playlists');
      }
    });
  }

  let show;
  if (playlist.cached) {
    show = (props =>
      <PlaylistShow {...props}
        playlist={playlist.details}
        key={playlist.id}
        rename={rename}
        changeVisibility={changeVisibility}
        addToSpotify={addToSpotify}
        withUsers={store.get('populateUsers')}
      />);
  } else {
    show = () => (<div className="d-flex justify-content-center flex-column" style={{height: 'calc(100vh-56px)'}}>
      <h2 className="text-center">Loading playlist...</h2>
      <div className="mt-2 d-flex justify-content-center">
        <Spinner animation="border" />
      </div>
    </div>);
    Client.getPlaylist(pid).then(res => {
      modifyPlaylist(pid, store, p => {
        p.details = res.playlist;
        p.cached = true;
      });
    });
  }

  return (
    <Switch>
      <Route exact path={match.url} render={show} />
      <Redirect to={match.url} />
    </Switch>
  );
}

export default withStore(Playlist, ['playlists']);
