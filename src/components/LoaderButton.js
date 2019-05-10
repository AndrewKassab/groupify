import React from 'react';
import { Button, Spinner } from 'react-bootstrap';

export default ({
  isLoading,
  text,
  loadingText,
  className = '',
  disabled = false,
  ...props
}) => (
  <Button
    className={className}
    disabled={disabled || isLoading}
    {...props}
  >
    {isLoading && <Spinner animation="border" />}
    {!isLoading ? text : loadingText}
  </Button>
);
