import React, { useState, useEffect } from 'react';
import Select from 'react-select';
import { Accordion, Card, Button, Spinner } from 'react-bootstrap';

import { spotifyPlaylists } from '../../../containers/mockdata';

const PlaylistSelector = ({ update, values, playlists, users }) => {
  const handleChange = (vals) => {
    update(vals);
  }

  const genCard = ({value, label, onChange}) => {
    const key = `create|u=${value}`;
    const [count, setCount] = useState(0);

    const handleChange = (playlists) => {
      setCount(playlists.length);
    }

    return (
      <Card key={key}>
        <Card.Header>
          <Accordion.Toggle eventKey={key} as={Button} variant="link" className="p-0 border-0">
            { label }
          </Accordion.Toggle>
          <span className="float-right">{ count } selected</span>
        </Card.Header>
        <Accordion.Collapse eventKey={key}>
          <Card.Body>
            <SelectPlaylists userId={value} onChange={handleChange} />
          </Card.Body>
        </Accordion.Collapse>
      </Card>
    );
  };

  return (
    <>
      <h3>Select Playlists:</h3>
      <Accordion>
        { users.map(genCard) }
        {
          users.length < 2 &&
          <Card><Card.Header>You must add another user</Card.Header></Card>
        }
      </Accordion>
    </>
  );
};

class SelectPlaylists extends React.Component {
  async = [];

  constructor(props) {
    super(props);

    this.state = {
      playlists: null,
    }
  }

  componentDidMount() {
    const handleResponse = (data) => {
      this.setState({playlists: data})
    };

    const d = spotifyPlaylists[this.props.userId] || [];
    const id = setTimeout(() => {
      console.log(d);
      handleResponse(d);
    }, 3000);

    this.async.push(id);
  }

  componentWillMount() {
    this.async.each((id) => clearTimeout(id));
  }

  render() {
    if (this.state.playlists === null) {
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
      const options = this.state.playlists.map(({name, id}) => {return {label: name, value: id}})
      return (
        <div style={{minHeight: "200px"}}>
          <Select
            placeholder='Playlists for user...'
            closeMenuOnSelect={false}
            isMulti
            options={options}
            onChange={this.props.onChange}
          />
        </div>
      );
    }
  }
};

export default PlaylistSelector;
