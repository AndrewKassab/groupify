import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelector from './create/UserSelector';
import PlaylistSelector from './create/PlaylistSelector';
import { userOptions, playlistOptions } from '../../containers/mockdata';


const defaultState = {
  show: false,
  users: [],
  playlists: [],
  page: 'users',
  next: 'Next',
};

class CreateModal extends Component {
  constructor(props) {
    super(props);

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.handleCancel = this.handleCancel.bind(this);

    this.updateUsers = this.updateUsers.bind(this);
    this.updatePlaylists = this.updatePlaylists.bind(this);

    this.state = defaultState;
    this.data = {
      users: [],
      playlists: []
    }
  }

  handleClose() {
    this.setState({ show: false });
  }

  handleShow() {
    this.setState({ show: true });
  }

  createPlaylist() {
    // dispatch requests or something
    // TODO: Actually save
    this.resetState();
  }

  resetState() {
    this.setState(defaultState);
    this.data = {users: [], playlists: []};
  }

  handleNext() {
    switch (this.state.page) {
      case 'users':
        this.setState({ page: 'playlists', next: 'Save' });
        break;

      case 'playlists':
        this.createPlaylist();
        break;

      default:
        this.resetState();
    }
  }

  handleCancel() {
    // Reset the form
    this.resetState();
  }

  updateUsers(users) {
    this.data.users = users;
    this.setState({users: users})
  }

  updatePlaylists(playlists) {
    this.data.playlists = playlists;
  }

  render() {
    return (
      <>
        <Button variant="outline-primary" onClick={this.handleShow}>
          Create Playlist
        </Button>

        <Modal show={this.state.show} onHide={this.handleClose} size="lg">
          <Modal.Header closeButton>
            <Modal.Title>Create Playlist</Modal.Title>
          </Modal.Header>
          <Modal.Body style={{minHeight: '200px'}}>
            <UserSelector update={this.updateUsers} options={userOptions} values={this.state.users} />
            <PlaylistSelector update={this.updatePlaylists} options={playlistOptions} values={this.state.playlists} users={this.state.users} />
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleCancel}>
              Cancel
            </Button>
            <Button variant="primary" onClick={this.handleNext}>
              { this.state.next }
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default CreateModal;
