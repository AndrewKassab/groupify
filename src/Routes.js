import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Home from './containers/Home';
import Signup from './containers/Signup';

export default () => (
  <Switch>
    <Route
      component={Home}
      exact
      path="/"
    />
    <Route
      component={Signup}
      exact
      path="/signup"
    />
  </Switch>
);
