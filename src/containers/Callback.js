import React, { Component } from 'react';
import { Row, Col, Container } from 'react-bootstrap';
import Background from '../images/logo.svg';

export default class Callback extends Component {
  render() {
    return (
      <div className="container h-100">
        <div className="row h-100 justify-content-center align-items-center">
          <form className="col-12">
            <div className="form-group">
              <label for="formGroupExampleInput">Example label</label>
              <input type="text" className="form-control" id="formGroupExampleInput" placeholder="Example input" />
            </div>
            <div className="form-group">
              <label for="formGroupExampleInput2">Another label</label>
              <input type="text" className="form-control" id="formGroupExampleInput2" placeholder="Another input" />
            </div>
          </form>
        </div>
      </div>
    );
  }
}
