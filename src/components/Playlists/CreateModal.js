import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelector from './create/UserSelector';
import PlaylistSelector from './create/PlaylistSelector';
import { userOptions, playlistOptions } from '../../containers/mockdata';

import Client from '../../Client';

const defaultState = {
  show: false,
  users: [],
  playlists: [],
  page: 'playlists',
  next: 'Next',
};

class CreateModal extends Component {
  constructor(props) {
    super(props);

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
    this.goBack = this.goBack.bind(this);

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
    this.data = {users: [], playlists: [], duration: 120};
  }

  handleNext() {
    console.log(this.data);

    switch (this.state.page) {
      case 'playlists':
        this.setState({ page: 'config', next: 'Save' });
        break;

      case 'config':
        this.createPlaylist();
        break;

      default:
        this.resetState();
    }
  }

  goBack() {
    this.setState({ page: 'playlists', next: 'Next' });
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
            {
              this.state.page === 'playlists' &&
              <Button variant="secondary" onClick={this.handleCancel}>
                Cancel
              </Button> ||
              <Button variant="secondary" onClick={this.goBack}>
                Go Back
              </Button>
            }
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
