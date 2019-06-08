import React, { Component } from 'react';
import { Row, Col, Container, ButtonToolbar, Button, Image } from 'react-bootstrap';
import Background from '../images/logo.svg';
import { Redirect } from 'react-router-dom';
import Client from '../Client';

export default class LoginPage extends Component {
  render() {
    if (Client.loggedIn()) {
      return <Redirect to="/playlists" />
    }

    return (
      <Container>
        <Row>
          <Col style={{height: '100vh'}} className="d-flex flex-column align-items-center py-3">
            <h1 className="text-center mb-2" > Groupify </h1>
            <h3 className="text-center mb-2" > Create a playlist that everyone can enjoy. </h3>
            <div className="flex-fill">
              <div className="mt-5 mb-2 d-flex justify-content-center flex-fill">
                <img src={Background} className="h-100 flex-shrink-1" />
              </div>
            </div>
            <div className="mb-4">
              <ButtonToolbar>
                <Button variant="outline-info" size="lg" block href="/api/signup">
                  Sign in using Spotify.
                </Button>
              </ButtonToolbar>
            </div>
          </Col>
        </Row>
      </Container>
    );
  }
}
