import React, { Component } from 'react';
import logo from '../images/logo.svg';

import { Row, Col, Container } from 'react-bootstrap';

export default class Main extends Component {
  render() {
    return (
      <Container>
        <Row>
          <Col md={4} lg={3}>
            {/* Sidebar */}
            <h1>Groupify</h1>
            <img
              alt="TeamLogo"
              className=""
              src={logo}
            />
            <p>Combine playlists at will.</p>
          </Col>
          <Col>
            {/* Content */}
            <h1>Hello, world!</h1>
          </Col>
        </Row>
      </Container>
    );
  }
}
