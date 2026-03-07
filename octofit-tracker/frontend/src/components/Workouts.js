import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const apiUrl = `http://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Workouts API endpoint:', apiUrl);
        console.log('Fetched workouts:', data);
        setWorkouts(data.results ? data.results : data);
      });
  }, [apiUrl]);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {workouts.map((workout, idx) => (
          <li key={idx}>{workout.name}: {workout.description} (Suggested for: {workout.suggested_for})</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
