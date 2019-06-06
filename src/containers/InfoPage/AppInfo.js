import React, { Component } from 'react';
import { Row, Col, Container, ButtonToolbar, Button, Image } from 'react-bootstrap';
import Background from '../images/logo.svg';
import { Redirect } from 'react-router-dom';
import Client from '../Client';
import Logo from '../../images/logo.svg';
import './AppInfo.css';

export default class InfoPage extends Component {
  render(){
    return (
      <Container>
        <div class="app-info">
          <h1>Groupify<img src="images/logo.svg" alt="Groupify Logo" height="60" width="60"/></h1> 
          <p>
            With Groupify you can create playlists that everyone is sure to enjoy.
            Whether you're just hanging out with friends or going for a drive, Groupify is sure to 
            generate a playlist where every user gets their fair share of music.
          </p>
          <p>
            Enjoy music together.
          </p>
          <h2>How It Works</h2>
          <p>
            Groupify will generate a playlist where every user gets a roughly 
            equal share of the track pool. By default, a user's track pool will consist 
            of a shuffled list of their most-played tracks over the past month. 
            You can replace this track pool with tracks from a pre-existing playlist 
            just by selecting it. Our algorithm will then go through each user's track pool and 
            add in songs, making sure to prioritize tracks that more group members are familiar 
            with. 
          </p>
          <p>
            The result is a playlist that reflects everyone's tastes!
          </p>
          <h3>
            I can't find my friend's Spotify accounts! <span role="img" arial-label="OMG" />
            😬
          </h3>
          <p>
            No problem at all! In order to create a group playlist with Spotify, each group member 
            in the group must have logged into Groupify before. Go ahead and send your friends 
            our link at 
            <a href="http://groupify.com/" target="_blank" rel="noopener noreferrer">
              groupify.com
            </a> and have them hit sign in. 
          </p>
          <p>
            You should now be set to find your friend and begin creating a playlist!
          </p>
          <h3>Spotify Access / Privacy</h3>
          <p>
            Application requires a Spotify account. It also needs access to your Spotify account.
            Application does not save your Spotify data and only accesses it for the purpose 
            of generating a playlist.
          </p>
        </div>
      </Container>
    );
  }
}