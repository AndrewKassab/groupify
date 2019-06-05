import React, { Component } from 'react';
import { Modal, Button, Spinner } from 'react-bootstrap';

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
  saving: false
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
    if (this.state.page !== 'save') {
      this.setState({ show: false });
    }
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
      const plist = res.playlist;
      this.props.store.get('reloadPlaylists')(`/playlists/${plist.id}`).then(() => {
        this.resetState();
      });
    });
  }

  resetState() {
    this.state.users.forEach(({id}) => {this.setState(updateData(id, []))});
    this.setState(defaultState);
    this.loadUsers();
  }

  handleNext() {
    switch (this.state.page) {
      case 'playlists':
        this.setState({ page: 'config', next: 'Create Playlist' });
        break;

      case 'config':
        this.setState({
          page: 'save',
          saving: true,
          next: 'Saving...'
        });
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

  backButton() {
    switch (this.state.page) {
      case 'playlists':
        return <Button variant="secondary" onClick={this.handleCancel}>Cancel</Button>;
      case 'config':
        return <Button variant="secondary" onClick={this.goBack}>Go Back</Button>;
    }
  }

  render() {
    const playlistShower = () => {
      switch(this.state.page) {
        case 'playlists':
          return (<>
            <UserSelector update={this.updateUsers} options={this.state.options} values={this.state.users} />
            <PlaylistSelector update={this.updatePlaylists} data={generateData(this.state)} />
          </>);

        case 'config':
          return <PlaylistParams updateName={this.updateName} updateDuration={this.updateDuration} name={this.state.name} duration={this.state.duration} />;

        case 'save':
          return (<div className="d-flex justify-content-center flex-column" style={{height: '200px'}}>
            <h2 className="text-center">Saving playlist...</h2>
            <div className="mt-2 d-flex justify-content-center">
              <Spinner animation="border" />
            </div>
          </div>);
      }
      if (this.state.page === 'playlists') {

      } else {
      }
    };

    return (
      <>
        <Button variant="outline-primary" onClick={this.handleShow}>
          Create Playlist
        </Button>

        <Modal show={this.state.show} onHide={this.handleClose} size="lg">
          <Modal.Header closeButton={!this.state.saving}>
            <Modal.Title>Create Playlist</Modal.Title>
          </Modal.Header>
          <Modal.Body style={{minHeight: '200px'}}>
            { !this.state.loading && playlistShower() }
          </Modal.Body>
          <Modal.Footer>
            { this.backButton() }
            <Button variant="primary" onClick={this.handleNext} disabled={this.state.users.length < 2 || this.state.saving}>
              { this.state.next }
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default withStore(CreateModal, ['users']);
