import React from 'react';
import {
  Navbar, Nav, NavDropdown, Container,
} from 'react-bootstrap';
// import { LinkContainer } from 'react-router-bootstrap';
import { Link } from 'react-router-dom';
import CreateModal from './components/Playlists/CreateModal';
import Client from './Client';

export default function Header() {
  return (
    <Navbar bg="dark" collapseOnSelect expand="md" variant="dark">
      <Container>
        <Navbar.Brand as={Link} to="/">Groupify</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse>
          <Nav className="mr-auto">
            <Nav.Link as={Link} to="/playlists">All Playlists</Nav.Link>
          </Nav>
          <Nav>
            <CreateModal />
            <Nav.Link onClick={Client.logout}>Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
