import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelect from './UserSelect';

class CreateModal extends Component {
  constructor(props, context) {
    super(props, context);

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleSave = this.handleSave.bind(this);
    this.handleCancel = this.handleCancel.bind(this);

    this.state = {
      show: false,
      users: [],
    };
  }

  handleClose() {
    this.setState({ show: false });
  }

  handleShow() {
    this.setState({ show: true });
  }

  handleSave() {
    // Save things
    this.handleClose();
  }

  handleCancel() {
    // Reset the form
    this.setState({
      show: false,
      users: [],
    });
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
            <UserSelect />
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleCancel}>
              Cancel
            </Button>
            <Button variant="primary" onClick={this.handleSave}>
              Next
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default CreateModal;
