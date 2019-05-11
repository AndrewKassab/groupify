import React from 'react';
import { Navbar, Nav, NavDropdown, Container } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
      <Navbar bg="dark" collapseOnSelect expand="md" variant="dark">
        <Container>
          <Navbar.Brand as={Link} to="/">Groupify</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link as={Link} to="/main">Main</Nav.Link>
              <Nav.Link href="#pricing">Pricing</Nav.Link>
              <NavDropdown id="collasible-nav-dropdown" title="Playlists">
                <NavDropdown.Item as={Link} to="/playlists">List Playlists</NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/playlists/1">Another action</NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/playlists/1/edit">Separated link</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item as={Link} to="/playlists/create">Something</NavDropdown.Item>
              </NavDropdown>
            </Nav>
            <Nav>
              <Nav.Link href="#deets">More deets</Nav.Link>
              <Nav.Link eventKey={2} href="#memes">
                Dank memes
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
  );
}
