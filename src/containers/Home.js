import React, { Component } from "react";
import logo from "../images/logo.svg";
import "./Home.css";

export default class Home extends Component {
  render() {
    return (
      <div className="Home">
        <div className="lander">
          <h1>Groupify</h1>
          <img src={logo} alt="TeamLogo" className="" />
          <p>Combine playlists at will.</p>
        </div>
      </div>
    );
  }
}
