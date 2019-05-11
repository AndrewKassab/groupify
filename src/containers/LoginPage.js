import React, { Component } from 'react';
import logo from '../images/logo.svg';

import { Row, Col, Container } from 'react-bootstrap';

export default class LoginPage extends Component {
  render() {
    return (
      <Container>
        <Row>
          <Col>
            <h1>Groupify</h1>
            <img
              alt="TeamLogo"
              className=""
              src={logo}
            />
            <p>Combine playlists at will.</p>
          </Col>
        </Row>
      </Container>
    );
  }
}
