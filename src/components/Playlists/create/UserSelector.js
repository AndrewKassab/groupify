import React from 'react';
import Select from 'react-select';

function UserSelector({ update, values, options }) {
  const handleChange = (values) => {
    update(values.map(({value, label}) => ({id: value, label: label})));
  };

  return (
    <>
      <h3>Add users:</h3>
      <Select
        placeholder='Users for playlist...'
        closeMenuOnSelect={false}
        isMulti
        options={options}
        value={values.map(({id, label}) => ({value: id, label: label}))}
        onChange={handleChange}
      />
    </>
  );
}

export default UserSelector;
