import React from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import LoginPage from './containers/LoginPage';
import Main from './containers/Main';
import Callback from './containers/Callback';
import Client from './Client';

const loggedIn = (
  <Switch>
    <Route component={Main} path="/playlists" />
    <Route render={() => <Redirect to='/playlists' />} />
  </Switch>
);

const notLoggedIn = (
  <Switch>
    <Route component={LoginPage} exact path="/" />
    <Route component={Callback} exact path="/callback" />
    <Route render={() => <Redirect to="/" />} />
  </Switch>
);

export default () => Client.loggedIn() ? loggedIn : notLoggedIn;
