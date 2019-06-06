import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';

import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';

import Routes from './Routes';
import { createStore } from '@spyna/react-store';

library.add(fas);

const defaultValues = {
  uid: null,
  users: [],
  playlists: [],
  redirect: null,
  lastId: -1,
}

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Routes />
      </BrowserRouter>
    );
  }
}

export default createStore(App, defaultValues);
