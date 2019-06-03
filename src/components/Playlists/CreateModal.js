import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelector from './create/UserSelector';
import PlaylistSelector from './create/PlaylistSelector';
import PlaylistParams from './create/PlaylistParams';
import { userOptions } from '../../containers/mockdata';

import Client from '../../Client';
import moment from 'moment';

const defaultState = {
  show: false,
  users: [],
  page: 'playlists',
  next: 'Next',
};

const generateData = (state) =>
  state.users.map(user => ({
    uid: user.id,
    label: user.label,
    playlists: state[pKey(user.id)]
  }));

const pKey = uid => `plist.${user.id}`;

const updateData = (uid, plist) => {
  return {
    [pKey(uid)]: plist
  };
}

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

    this.updateDuration = this.updateDuration.bind(this);
    this.updateName = this.updateName.bind(this);

    this.state = defaultState;

    this.state.name = moment().format('[Groupify -] MMM Do YYYY, h:mm a');
    this.state.duration = 60;
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
    this.setState({users: users});
  }

  updatePlaylists(uid, playlists) {
    this.setState(updateData(uid, playlists));
  }

  updateName(name) {
    this.setState({name: name});
  }

  updateDuration(duration) {
    this.setState({duration: parseInt(duration)});
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
            {
              this.state.page === 'playlists' && (<>
                <UserSelector update={this.updateUsers} options={userOptions} values={this.state.users} />
                <PlaylistSelector update={this.updatePlaylists} values={generateData(this.state)} />
              </>) ||
              <PlaylistParams updateName={this.updateName} updateDuration={this.updateDuration} name={this.state.name} duration={this.state.duration} />
            }
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
            <Button variant="primary" onClick={this.handleNext} disabled={this.state.users.length < 2}>
              { this.state.next }
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default CreateModal;
