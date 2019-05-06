import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import Signup from "./containers/Signup";

export default () =>
  <Switch>
    <Route path="/" exact component={Home} />
    <Route path="/signup" exact component={Signup} />
  </Switch>;
