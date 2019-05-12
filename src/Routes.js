import React from 'react';
import { Route, Switch } from 'react-router-dom';
import LoginPage from './containers/LoginPage';
import Main from './containers/Main';

export default () => (
  <Switch>
    <Route exact path="/" component={LoginPage} />
    <Route exact path="/main" component={Main} />
  </Switch>
);
