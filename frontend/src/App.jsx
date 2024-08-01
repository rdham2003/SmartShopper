import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';
import axios from 'axios';
import HomePage from './HomePage';
import {createBrowserRouter,RouterProvider, Route, Link} from "react-router-dom";
import Survey from './Survey';
import Search from './Search';

function App() {
  const [data, setData] = useState({ "Deals": [], "Rated": [], "Survey": [], "Search": [], "searchOn": false, "incPass": false, "signinErr": false});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/data");
        setData(response.data);
        // console.log(response.data);
      } catch (error) {
        console.error('There was an error fetching the data!', error);
      }
    };

    fetchData();
  }, []);

  // console.log(data.Deals)
  // console.log(data.Rated)
  // console.log(data.Survey)
  
  return (
    <Fragment>
      <HomePage rated={data.Rated} deals={data.Deals} survey={data.Survey} search = {data.Search} searchOn = {data.searchOn} incPass = {data.incPass} signinErr = {data.signinErr}/>
    </Fragment>
  );
}

export default App;