import React from 'react';
import Select from 'react-select';

class UserSelector extends React.Component {
  state = {
    selectedOption: null,
  }
  handleChange = (selectedOption) => {
    this.setState({ selectedOption });
    console.log(`Option selected:`, selectedOption);
  }

  render() {
    return (
      <Select
        isMulti
      />
    );
  }
}

export default UserSelector;
