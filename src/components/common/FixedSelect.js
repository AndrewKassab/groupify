import React, { Component } from 'react';

import Select from 'react-select';

const styles = {
  multiValue: (base, state) => {
    return state.data.isFixed ? { ...base, backgroundColor: 'gray' } : base;
  },
  multiValueLabel: (base, state) => {
    return state.data.isFixed ? { ...base, fontWeight: 'bold', color: 'white', paddingRight: 6 } : base;
  },
  multiValueRemove: (base, state) => {
    return state.data.isFixed ? { ...base, display: 'none' } : base;
  }
};

const orderOptions = (values) => {
  return values.filter((v) => v.isFixed).concat(values.filter((v) => !v.isFixed));
};

export default class FixedSelect extends Component {
  constructor(props) {
    super(props);

    this.onChange = this.onChange.bind(this);
    this.state = {
      value: this.props.value
    }
  }

  fixedOptions() {
    return this.props.options.filter((v) => v.isFixed);
  }

  onChange (value, { action, removedValue }) {
    switch (action) {
      case 'remove-value':
      case 'pop-value':
        if (removedValue.isFixed) {
          return;
        }
        break;
      case 'clear':
        value = this.fixedOptions();
        break;
    }

    value = orderOptions(value);
    this.setState({ value: value });

    if (this.props.onChange) {
      this.props.onChange(value);
    }
  }

  render() {
    return (
      <Select
        { ...this.props }
        value={orderOptions(this.state.value)}
        isMulti
        styles={styles}
        isClearable={this.state.value.some(v => !v.isFixed)}
        name="colors"
        onChange={this.onChange}
        options={this.props.options}
      />
    );
  }
}
