import {
  Nav, Navbar, Card, Container, Row, Col, FormControl, InputGroup, Button, Form,
} from 'react-bootstrap';
import React, { Component } from 'react';

export default class UserSelect extends Component {
  render() {
    return (
      <Container fluid="true">
        <Row>
          <Col>
            <div className="row h-100">
              <div className="col-sm-8 align-self-center">
                <div className="card card-block">
                  <label>Search for Users</label>
                  <InputGroup>
                    <FormControl
                      aria-describedby="basic-addon2"
                      aria-label="New Playlist Name"
                      placeholder="(Ex: JDoe123)"
                    />
                    <InputGroup.Append>
                      <Button>Search</Button>
                    </InputGroup.Append>
                  </InputGroup>
                </div>
              </div>
            </div>
          </Col>
        </Row>
        <Row>
          <div className="col-sm-8 align-self-center">
            <Form.Group controlId="exampleForm.ControlSelect2">
              <Form.Label>Select users</Form.Label>
              <Form.Control as="select" multiple>
                <option>Person 1 (username1)</option>
                <option>Person 2 (username2)</option>
                <option>Person 3 (username3)</option>
                <option>Person 4 (username4)</option>
                <option>Person 5 (username5)</option>
                <option>Person 6 (username6)</option>
                <option>Person 7 (username7)</option>
                <option>Person 8 (username8)</option>
                <option>Person 9 (username9)</option>
                <option>Person 10 (username10)</option>
                <option>Person 11 (username11)</option>
              </Form.Control>
            </Form.Group>
          </div>
          <Button style={{ height: '50px', marginTop: '50px' }}>
            Add to Group
            </Button>
        </Row>
        <Row>
          <label>Users in group: Person 2, Person 3</label>
        </Row>
      </Container>
    );
  }
}
