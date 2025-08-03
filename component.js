import React, { useState } from 'react';

function Task07Component() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h3>Task 07: useState</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Task07Component;
