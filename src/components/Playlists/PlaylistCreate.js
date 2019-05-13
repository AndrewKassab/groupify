import React, { Component } from 'react';
import { Form } from 'react-bootstrap';

export default class PlaylistCreate extends Component {
  constructor(props) {
    super(props);
    this.state = {
      kanye: true,
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  render() {
    return (
      <div>

        {/* Content */}
        <br></br>
        <br></br>
        <p>Select playlists to draw songs from:</p>

        <label>
          kanye
            <input
            name="kanye"
            type="checkbox"
            checked={this.state.kanye}
            onChange={this.handleInputChange} />
        </label>
        <br></br>
        <label>
          lofi beats to study
            <input
            name="lofi"
            type="checkbox"
            checked={this.state.lofi}
            onChange={this.handleInputChange} />
        </label>
        <br></br>
        <label>
          Christmas Music
            <input
            name="christmas"
            type="checkbox"
            checked={this.state.isGoing}
            onChange={this.handleInputChange} />
        </label>
        <br></br>
        <label>
          3 am music
            <input
            name="3am"
            type="checkbox"
            checked={this.state.am}
            onChange={this.handleInputChange} />
        </label>
        <br></br>
        <label>
          turn up
            <input
            name="turnup"
            type="checkbox"
            checked={this.state.turnup}
            onChange={this.handleInputChange} />
        </label>

        <br></br>
        <br></br>
        <p>Select playlist length:</p>
        <select>
          <option selected value="30">30:00</option>
          <option value="45">45:00</option>
          <option value="100">1:00:00</option>
          <option value="115">1:15:00</option>
          <option value="130">1:30:00</option>
          <option value="145">1:45:00</option>
          <option value="200">2:00:00</option>
        </select>
        <br></br>
        <br />
        <input type="submit" value="Create Playlist" />
      </div>
    );
  }
}
