import React from 'react';
import { Route, Switch } from 'react-router-dom';
import LoginPage from './containers/LoginPage';
import Main from './containers/Main';

export default () => (
  <Switch>
    <Route
      component={LoginPage}
      exact
      path="/"
    />
    <Route
      component={Main}
      exact
      path="/main"
    />
  </Switch>
);
