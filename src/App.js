import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';

import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';

// To add a FontAwesome icon:
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import Routes from './Routes';
import Header from './Header';

library.add(fas);

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
