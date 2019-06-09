import React, { Component } from 'react';
import { Alert, Modal, Button, Spinner } from 'react-bootstrap';

import UserSelector from './create/UserSelector';
import PlaylistSelector from './create/PlaylistSelector';
import PlaylistParams from './create/PlaylistParams';

import { withStore } from '@spyna/react-store';

import Client, { modifyPlaylist } from '../../Client';
import moment from 'moment';

const defaultState = {
  loading: null,
  name: null,
  duration: 60,
  show: false,
  users: [],
  page: 'playlists',
  next: 'Next',
  saving: false,
  save: false,
  failed: false,
  lastId: -1,
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
    this.updateSave = this.updateSave.bind(this);
    this.populateUsers = this.populateUsers.bind(this);

    this.state = defaultState;
  }

  populateUsers(userIds=[]) {
    this.loadUsers().then((opts) => {
      const options = opts.filter(({id}) => userIds.includes(id)).sort((u1, u2) => u1.isFixed ? -1 : 1)
      this.setState({users: options});
    });
    this.handleShow();
  }

  handleClose() {
    if (this.state.page !== 'save') {
      this.setState({ show: false });
    }
  }

  handleShow() {
    if (this.state.loading === null) {
      this.loadUsers();
    }
    this.setState({show: true});
  }

  createPlaylist() {
    const { name, duration, users, save } = this.state;
    const { store } = this.props;
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

      store.set('redirect', `/playlists/${plist.id}`);
      Client.manualPoll().then(() => {
        this.resetState();
      });

      if (save) {
        const id = plist.id;
        Client.addToSpotify(id).then(res => {
          modifyPlaylist(id, store, p => {
            p.details.spotify_id = res.spotify_id;
          });
        });
      }
    }).catch(e => {
      this.setState({failed: true, saving: false, page: 'config', next: 'Create Playlist'});
    });
  }

  resetState() {
    this.state.users.forEach(({id}) => {this.setState(updateData(id, []))});
    this.setState(defaultState);
  }

  handleNext() {
    if (!this.state.name) {
      this.setState({name: moment().format('[Groupify -] MMM Do YYYY, h:mm a')});
    }

    switch (this.state.page) {
      case 'playlists':
        this.setState({ page: 'config', next: 'Create Playlist' });
        break;

      case 'config':
        this.setState({
          page: 'save',
          saving: true,
          next: 'Generating...'
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

  updateSave(save) {
    this.setState({save: save})
  }

  loadUsers() {
    this.setState({loading: true})

    return Client.listUsers().then(res => {
      const uid = Client.userId();
      const options = res.users.map(({id, name, username}) => ({
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

      return options;
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

  componentDidMount() {
    const { store } = this.props;

    store.set('populateUsers', this.populateUsers)
  }

  render() {
    const playlistShower = () => {
      switch(this.state.page) {
        case 'playlists':
          return (<>
            <UserSelector
              className="mb-3"
              update={this.updateUsers}
              options={this.state.options}
              values={this.state.users}
            />
            <PlaylistSelector
              update={this.updatePlaylists}
              data={generateData(this.state)}
            />
          </>);

        case 'config':
          return (
            <PlaylistParams
              updateName={this.updateName}
              updateDuration={this.updateDuration}
              updateSave={this.updateSave}
              name={this.state.name}
              duration={this.state.duration}
              save={this.state.save}
            />
          );

        case 'save':
          return (<div className="d-flex justify-content-center flex-column" style={{height: '200px'}}>
            <h2 className="text-center">Generating playlist...</h2>
            <div className="mt-2 d-flex justify-content-center">
              <Spinner animation="border" />
            </div>
          </div>);
      }
    };

    const { saving, users, page, name } = this.state;
    const disableNext = users.length < 2 || saving || (page === 'config' && !name);

    return (
      <>
        <Button variant="outline-primary" onClick={this.handleShow} className="mr-md-2">
          Create Playlist
        </Button>

        <Modal show={this.state.show} onHide={this.handleClose} size="lg">
          <Modal.Header closeButton={!this.state.saving}>
            <Modal.Title>Create Playlist</Modal.Title>
          </Modal.Header>
          <Modal.Body style={{minHeight: '200px'}}>
            { this.state.failed && <Alert variant="danger">Error: unable to create Playlist</Alert> }
            {
              this.state.loading ?
              (<div className="d-flex justify-content-center flex-column" style={{height: '200px'}}>
                <h2 className="text-center">Loading data...</h2>
                <div className="mt-2 d-flex justify-content-center">
                  <Spinner animation="border" />
                </div>
              </div>) :
              playlistShower()
            }
          </Modal.Body>
          <Modal.Footer>
            { this.backButton() }
            <Button variant="primary"
              onClick={this.handleNext}
              disabled={disableNext}
            >
              { this.state.next }
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default withStore(CreateModal, ['users']);
