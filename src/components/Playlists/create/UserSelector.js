import React from 'react';
import Select from 'react-select';
import FixedSelect from '../../common/FixedSelect';

function UserSelector({ update, values, options }) {
  const handleChange = (values) => {
    update(values);
  };

  return (
    <>
      <h3>Add users:</h3>
      <FixedSelect
        placeholder='Users for playlist...'
        closeMenuOnSelect={false}
        isMulti
        options={options}
        value={values}
        onChange={handleChange}
      />
    </>
  );
}

export default UserSelector;
