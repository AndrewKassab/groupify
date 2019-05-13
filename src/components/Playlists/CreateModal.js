import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelect from './UserSelect';
import PlaylistCreate from './PlaylistCreate';

class CreateModal extends Component {
  constructor(props, context) {
    super(props, context);

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.handleCancel = this.handleCancel.bind(this);

    this.state = {
      show: false,
      users: [],
      page: 'users',
      next: 'Next',
    };
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
    this.setState({
      show: false,
      users: [],
      page: 'users',
      next: 'Next',
    });
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
          <Modal.Body>
            {
              this.state.page == 'users' ?
              <UserSelect /> :
              <PlaylistCreate />
            }
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
