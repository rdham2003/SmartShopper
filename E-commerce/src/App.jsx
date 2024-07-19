import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';
import axios from 'axios';
import HomePage from './HomePage'
import Survey from './Survey'

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('/home');
      setData(response.data.members);
    };
    fetchData();
  }, []);

  return (
    <Fragment>
      <Survey />
      <HomePage data={data}/>
    </Fragment>
  );
}

export default App;
