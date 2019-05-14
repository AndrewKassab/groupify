import React, { Component } from 'react';
import { Row, Col, Container } from 'react-bootstrap';
import { Switch, Route } from 'react-router';
import PlaylistList from '../components/Playlists/PlaylistList';
import Playlist from '../components/Playlists/Playlist';
import mockdata from './mockdata';


export default class Main extends Component {
  constructor(props) {
    super(props);

    this.state = {
      playlists: mockdata.playlists,
    };
  }

  render() {
    return (
      <Container className="mt-3">
        <Row>
          <Col lg={3} md={4}>
            <PlaylistList playlists={this.state.playlists} />
          </Col>
          <Col className="ml-sm-auto">
            <Switch>
              <Route path="/playlists/:id" render={props => <Playlist {...props} playlists={this.state.playlists} />} />
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
    <h3 className="text-muted text-center mt-5">Please select a playlist</h3>
  );
}
