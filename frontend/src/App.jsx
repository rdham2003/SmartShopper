import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';
import axios from 'axios';
import HomePage from './HomePage';
import Survey from './Survey';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/data");
        setData(response.data);
        console.log(response.data);
      } catch (error) {
        console.error('There was an error fetching the data!', error);
      }
    };

    fetchData();
  }, []);

  console.log(data)
  return (
    <Fragment>
      {/* <Survey /> */}
      <HomePage rated={[[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]} deals={[[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]}/>
    </Fragment>
  );
}

export default App;