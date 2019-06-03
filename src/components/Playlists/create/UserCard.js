import React, { useState } from 'react';
import Select from 'react-select';
import { Accordion, Card, Button, Spinner } from 'react-bootstrap';
import Client from '../../../Client';

const UserCard = ({uid, label, playlists, onChange}) => {
  const key = `create|u=${uid}`;
  const [count, setCount] = useState(playlists.length);

  const handleChange = (playlists) => {
    setCount(playlists.length);
    onChange(uid, playlists);
  }

  return (
    <Card>
      <Accordion.Toggle eventKey={key} as={Card.Header} >
        { label }
        <span className="float-right">{ count } selected</span>
      </Accordion.Toggle>
      <Accordion.Collapse eventKey={key}>
        <Card.Body>
          <SelectPlaylists userId={uid} onChange={handleChange} selected={playlists} />
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  );
};

class SelectPlaylists extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true
    };
  }

  componentDidMount() {
    Client.spotifyPlaylists(uid).then(plists => {
      const options = plists.map(({name, spotify_id}) => ({label: name, value: spotify_id}));

      this.setState({
        loading: false,
        options: options
      });
    });
  }

  render() {
    if (this.state.loading) {
      return (
        <div className="d-flex justify-content-center">
          <Button variant="primary" disabled>
            <Spinner
              as="span"
              animation="grow"
              size="sm"
              role="status"
              aria-hidden="true"
            />
            Loading...
          </Button>
        </div>
      );
    } else {
      return (
        <div style={{minHeight: "200px"}}>
          <Select
            placeholder='Playlists for user...'
            closeMenuOnSelect={false}
            isMulti
            options={this.state.options}
            onChange={this.props.onChange}
            defaultValue={this.props.selected}
          />
        </div>
      );
    }
  }
};

export default UserCard;
