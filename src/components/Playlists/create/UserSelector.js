import React from 'react';
import FixedSelect from '../../common/FixedSelect';

function UserSelector({ update, values, options, className }) {
  const handleChange = (values) => {
    update(values);
  };

  return (
    <div className={className}>
      <h3 className="mb-3">Add Group Members:</h3>
      <FixedSelect
        placeholder='Users for playlist...'
        closeMenuOnSelect={false}
        isMulti
        options={options}
        value={values}
        onChange={handleChange}
      />
    </div>
  );
}

export default UserSelector;
