import React from 'react';

function Form() {
  return (
    <form>
      <label>
        Name:
        <input type="text" />
      </label>
      <label>
        Email:
        <input type="email" />
      </label>
      <button>Submit</button>
    </form>
  );
}

export default Form;