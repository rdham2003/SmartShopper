import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';
import axios from 'axios';
import HomePage from './HomePage'
import Survey from './Survey'

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://localhost:5000")
      const info = await response.json()
      setData(info.data)
      console.log(info.data)
    }
  })

  return (
    <Fragment>
      <Survey />
      <HomePage data={data}/>
    </Fragment>
  );
}

export default App;
