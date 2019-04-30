import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Spotify from 'spotify-web-api-js'

const spotifyWebApi = new Spotify();

/**
 * TODO: Complete
 */
class LoggedIn extends Component {
  constructor(){
    super();
  }
  render(){
    return (
      <div>
        <h>You are now a logged in user</h>
      </div>
    );
  }
}
