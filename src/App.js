import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Header from './Header';
import Routes from './Routes';

export default class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Header />
          <Routes />
        </div>
      </BrowserRouter>
    );
  }
}
