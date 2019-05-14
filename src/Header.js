import React from 'react';
import {
  Navbar, Nav, NavDropdown, Container,
} from 'react-bootstrap';
// import { LinkContainer } from 'react-router-bootstrap';
import { Link } from 'react-router-dom';
import CreateModal from './components/Playlists/CreateModal';

export default function Header() {
  return (
    <Navbar bg="dark" collapseOnSelect expand="md" variant="dark">
      <Container>
        <Navbar.Brand as={Link} to="/">Groupify</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse>
          <Nav className="mr-auto">
            <Nav.Link as={Link} to="/playlists">All Playlists</Nav.Link>
            {/* <NavDropdown id="collasible-nav-dropdown" title="Playlists">
              <NavDropdown.Item as={Link} to="/playlists">List Playlists</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/playlists/1">View Playlist (id: 1)</NavDropdown.Item>
            </NavDropdown> */}
          </Nav>
          <Nav>
            <CreateModal />
            <Nav.Link as={Link} to="/logout">Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
