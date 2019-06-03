import React from 'react';
import { Route, Switch } from 'react-router-dom';
import LoginPage from './containers/LoginPage';
import Main from './containers/Main';
import Callback from './containers/Callback';

export default () => (
  <Switch>
    <Route component={LoginPage} exact path="/" />
    <Route component={Main} path="/playlists" />
    <Route component={Callback} path="/callback" />
  </Switch>
);
