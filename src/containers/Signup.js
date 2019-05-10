import React, { Component } from 'react';
import {
  FormGroup,
  FormControl,
  FormLabel,
} from 'react-bootstrap';
import LoaderButton from '../components/LoaderButton';

export default class Signup extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      email: '',
      password: '',
      confirmPassword: '',
      confirmationCode: '',
      newUser: null,
    };
  }

  validateForm() {
    return (
      this.state.email.length > 0
      && this.state.password.length > 0
      && this.state.password === this.state.confirmPassword
    );
  }

  validateConfirmationForm() {
    return this.state.confirmationCode.length > 0;
  }

  handleChange = (event) => {
    this.setState({
      [event.target.id]: event.target.value,
    });
  }

  handleSubmit = async (event) => {
    event.preventDefault();

    this.setState({ isLoading: true });
    this.setState({ newUser: 'test' });
    this.setState({ isLoading: false });
  }

  handleConfirmationSubmit = async (event) => {
    event.preventDefault();

    this.setState({ isLoading: true });
  }

  renderConfirmationForm() {
    return (
      <form onSubmit={this.handleConfirmationSubmit}>
        <FormGroup
          bsSize="large"
          controlId="confirmationCode"
        >
          <FormLabel>Confirmation Code</FormLabel>
          <FormControl
            autoFocus
            onChange={this.handleChange}
            type="tel"
            value={this.state.confirmationCode}
          />
        </FormGroup>
        <LoaderButton
          block
          bsSize="large"
          disabled={!this.validateConfirmationForm()}
          isLoading={this.state.isLoading}
          loadingText="Verifying…"
          text="Verify"
          type="submit"
        />
      </form>
    );
  }

  renderForm() {
    return (
      <form onSubmit={this.handleSubmit}>
        <FormGroup
          bsSize="large"
          controlId="email"
        >
          <FormLabel>Email</FormLabel>
          <FormControl
            autoFocus
            onChange={this.handleChange}
            type="email"
            value={this.state.email}
          />
        </FormGroup>
        <FormGroup
          bsSize="large"
          controlId="password"
        >
          <FormLabel>Password</FormLabel>
          <FormControl
            onChange={this.handleChange}
            type="password"
            value={this.state.password}
          />
        </FormGroup>
        <FormGroup
          bsSize="large"
          controlId="confirmPassword"
        >
          <FormLabel>Confirm Password</FormLabel>
          <FormControl
            onChange={this.handleChange}
            type="password"
            value={this.state.confirmPassword}
          />
        </FormGroup>
        <LoaderButton
          block
          bsSize="large"
          disabled={!this.validateForm()}
          isLoading={this.state.isLoading}
          loadingText="Signing up…"
          text="Signup"
          type="submit"
        />
      </form>
    );
  }

  render() {
    return (
      <div className="Signup">
        {this.state.newUser === null
          ? this.renderForm()
          : this.renderConfirmationForm()}
      </div>
    );
  }
}
