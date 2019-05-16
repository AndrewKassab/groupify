import React from 'react';
import { Form } from 'react-bootstrap';

class PlaylistCreate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      kanye: true,
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const { target } = event;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    this.setState({
      [name]: value,
    });
  }

  render() {
    return (
      <div>

        {/* Content */}
        <p>Select playlists to draw songs from:</p>

        <label>
          kanye
          <input
            checked={this.state.kanye}
            name="kanye"
            onChange={this.handleInputChange}
            type="checkbox"
          />
        </label>
        <br />
        <label>
          lofi beats to study
          <input
            checked={this.state.lofi}
            name="lofi"
            onChange={this.handleInputChange}
            type="checkbox"
          />
        </label>
        <br />
        <label>
          Christmas Music
          <input
            checked={this.state.isGoing}
            name="christmas"
            onChange={this.handleInputChange}
            type="checkbox"
          />
        </label>
        <br />
        <label>
          3 am music
          <input
            checked={this.state.am}
            name="3am"
            onChange={this.handleInputChange}
            type="checkbox"
          />
        </label>
        <br />
        <label>
          turn up
          <input
            checked={this.state.turnup}
            name="turnup"
            onChange={this.handleInputChange}
            type="checkbox"
          />
        </label>

        <br />
        <br />
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
      </div>
    );
  }
}

export default PlaylistCreate;
