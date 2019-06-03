import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';

import UserSelector from './create/UserSelector';
import PlaylistSelector from './create/PlaylistSelector';
import PlaylistParams from './create/PlaylistParams';

import { withStore } from '@spyna/react-store';

import Client from '../../Client';
import moment from 'moment';

const defaultState = {
  loading: true,
  name: null,
  duration: 60,
  show: false,
  users: [],
  page: 'playlists',
  next: 'Next',
};

const generateData = (state) =>
  state.users.map(user => ({
    uid: user.id,
    label: user.label,
    username: user.username,
    playlists: state[pKey(user.id)] || []
  }));

const pKey = uid => `plist.${uid}`;

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
    this.createPlaylist = this.createPlaylist.bind(this);

    this.updateDuration = this.updateDuration.bind(this);
    this.updateName = this.updateName.bind(this);

    this.state = defaultState;

    this.loadUsers();
  }

  handleClose() {
    this.setState({ show: false });
  }

  handleShow() {
    let update = {show: true}

    if (!this.state.name) {
      update.name = moment().format('[Groupify -] MMM Do YYYY, h:mm a')
    }

    this.setState(update);
  }

  createPlaylist() {
    const { name, duration, users } = this.state;
    const userList = users.map(u => u.id);
    const playlists = generateData(this.state).map(
      ({playlists}) => playlists.map(p => p.value)
    ).flat();
    let userPlaylists = {};
    generateData(this.state).map(({username, playlists}) => {
      userPlaylists[username] = playlists.map(p => p.value);
    });

    Client.createPlaylist(name, userList, playlists, duration, userPlaylists).then(res => {
      console.log(res);
      this.props.store.get('reloadPlaylists')();
    });
    // dispatch requests or something
    // TODO: Actually save
    this.resetState();
  }

  resetState() {
    this.setState(defaultState);
    this.loadUsers();
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

  loadUsers() {
    Client.listUsers().then(res => {
      const uid = Client.userId();
      let options = res.users.map(({id, name, username}) => ({
        label: `${name} - ${username}`,
        value: id,
        username: username,
        id: id,
        isFixed: (id === uid),
      }));

      this.setState({
        options: options,
        loading: false,
        users: options.filter(({isFixed}) => isFixed)
      });
    });
  }

  render() {
    const playlistShower = () => {
      if (this.state.page === 'playlists') {
        return (<>
          <UserSelector update={this.updateUsers} options={this.state.options} values={this.state.users} />
          <PlaylistSelector update={this.updatePlaylists} data={generateData(this.state)} />
        </>);
      } else {
        return <PlaylistParams updateName={this.updateName} updateDuration={this.updateDuration} name={this.state.name} duration={this.state.duration} />;
      }
    };

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
            { !this.state.loading && playlistShower() }
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

export default withStore(CreateModal, ['users']);
