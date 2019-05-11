import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Header from './Header';
import Routes from './Routes';

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'

library.add(fas)

// To add a FontAwesome icon:
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

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
