import React, { Component } from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';
import { Nav, Navbar } from 'react-bootstrap';
import './App.css';
import Header from './Header';
import Routes from './Routes';

export default class App extends Component {
  render() {
    return (
      <Router>
        <div className="App container">
          <Header />
          <Navbar collapseOnSelect fluid>
            <Navbar.Brand>
              <Link to="/">Groupify</Link>
            </Navbar.Brand>

            <Navbar.Collapse>
              <Nav pullRight>
                <Nav.Item><Link to="/signup">Sign up or log in using Spotify.</Link></Nav.Item>
              </Nav>
            </Navbar.Collapse>
          </Navbar>

          <Routes />
        </div>
      </Router>
    );
  }
}
