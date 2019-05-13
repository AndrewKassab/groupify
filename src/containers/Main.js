import React, { Component } from 'react';
import PlaylistList from '../components/Playlists/PlaylistList';
import Playlist from '../components/Playlists/Playlist';

import { Row, Col, Container } from 'react-bootstrap';
import { Switch, Route } from 'react-router';

export default class Main extends Component {
  constructor(props) {
    super(props);

    this.state = {
      playlists: [
        {id: 1, name: "Hello world", tracks: [
          {id: 1, name: 'blah'},
          {id: 2, name: 'blah2'}
        ]},
        {id: 2, name: "Other playlist", tracks: [
          {id: 3, name: "other"},
        ]},
      ]
    }
  }

  render() {
    return (
      <Container className='mt-3'>
        <Row>
          <Col md={4} lg={3} className="h-100 position-fixed">
            <PlaylistList playlists={this.state.playlists} />
          </Col>
          <Col className="ml-sm-auto">
            <Switch>
              <Route path="/playlists/:id" render={props => <Playlist {...props} playlists={this.state.playlists} />} />
              {/* <Route render={() => <h3>Please choose a playlist</h3>} /> */}
              <Route component={NoPlaylist} />
            </Switch>
          </Col>
        </Row>
      </Container>
    );
  }
}

function NoPlaylist() {
  return (
    <Container fluid className="h-100">
      <Row className="h-100">
        <Col className="align-self-center">
          <div className="card card-block">
            Center
          </div>
        </Col>
      </Row>
    </Container>
  );
}
