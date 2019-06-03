import React, { Component } from 'react';
import { Row, Col, Container } from 'react-bootstrap';
import { Switch, Route } from 'react-router';
import PlaylistList from '../components/Playlists/PlaylistList';
import Playlist from '../components/Playlists/Playlist';
import mockdata from './mockdata';
import Client from '../Client';
import Header from '../Header';

import { withStore } from '@spyna/react-store';

class Main extends Component {
  constructor(props) {
    super(props);

    this.reloadPlaylists = this.reloadPlaylists.bind(this);
  }

  componentDidMount() {
    const { store } = this.props;

    store.set('uid', Client.userId());
    store.set('reloadPlaylists', this.reloadPlaylists)

    this.reloadPlaylists();
  }

  reloadPlaylists() {
    const { store } = this.props;

    Client.listPlaylists().then(res => {
      const plists = res.playlists.sort((a, b) => b.id - a.id);
      store.set('playlists', plists);
    });
  }

  render() {
    return (
      <div>
        <Header />
        <Container className="mt-3">
          <Row>
            <Col lg={3} md={4}>
              <PlaylistList />
            </Col>
            <Col className="ml-sm-auto">
              <Switch>
                <Route path="/playlists/:id" render={props => <Playlist {...props} />} />
                <Route component={NoPlaylist} />
              </Switch>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

function NoPlaylist() {
  return (
    <h3 className="text-muted text-center mt-5">Please select a playlist</h3>
  );
}

export default withStore(Main);
