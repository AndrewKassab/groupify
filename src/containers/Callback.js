import React, { Component } from 'react';
import { Row, Col, Container, Spinner } from 'react-bootstrap';
import Client from '../Client';

const Callback = ({history, location}) => {
  Client.login(location.search, history);

  return (
    <div className="container h-100">
      <div className="row h-100 justify-content-center align-items-center">
        <Spinner animation="border" />
      </div>
    </div>
  );
};


export default Callback;
