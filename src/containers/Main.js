import React, { Component } from 'react';
import { Row, Col, Container } from 'react-bootstrap';
import { Switch, Route } from 'react-router';
import PlaylistList from '../components/Playlists/PlaylistList';
import Playlist from '../components/Playlists/Playlist';
import Client from '../Client';
import Header from '../Header';

import { withStore } from '@spyna/react-store';

class Main extends Component {
  constructor(props) {
    super(props);

    Client.whoAmI();

    this.reloadPlaylists = this.reloadPlaylists.bind(this);
  }

  componentDidMount() {
    const { store } = this.props;

    store.set('reloadPlaylists', this.reloadPlaylists);

    this.reloadPlaylists();

    Client.startPoll(({previous, latest}) => {
      if (previous.playlists !== latest.playlists) {
        this.reloadPlaylists(store.get('redirect'));
        store.set('redirect', null);
      }

      if (previous.users !== latest.users) {
        store.set('lastId', latest.users)
      }
    });
  }

  componentWillUnmount() {
    Client.stopPolling();
  }

  reloadPlaylists(redirect = null) {
    const { store } = this.props;

    return Client.listPlaylists().then(res => {
      const plists = res.playlists.sort((a, b) => b.id - a.id);
      store.set('playlists', plists);
    }).then(() => {
      if (redirect) {
        this.props.history.push(redirect);
      }
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
                <Route path="/playlists/:id" component={Playlist} />
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
