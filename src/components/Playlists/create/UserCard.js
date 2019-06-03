import React, { useState } from 'react';
import Select from 'react-select';
import { Accordion, Card, Button, Spinner } from 'react-bootstrap';
import { spotifyPlaylists } from '../../../containers/mockdata';

const UserCard = ({value, label, onChange}) => {
  const key = `create|u=${value}`;
  const [count, setCount] = useState(0);

  const handleChange = (playlists) => {
    setCount(playlists.length);
    onChange(value, playlists);
  }

  return (
    <Card>
      <Accordion.Toggle eventKey={key} as={Card.Header} >
        { label }
        <span className="float-right">{ count } selected</span>
      </Accordion.Toggle>
      <Accordion.Collapse eventKey={key}>
        <Card.Body>
          <SelectPlaylists userId={value} onChange={handleChange} />
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  );
};

class SelectPlaylists extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      playlists: null,
    };

    this.async = [];
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

  componentWillUnmount() {
    this.async.forEach((id) => clearTimeout(id));
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

export default UserCard;
