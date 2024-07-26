import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';

function Brands(){

    function toHome(){
        document.getElementById("homePage").style.display = "block"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
      }
      function toAboutUs(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "block"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
      }

      function toBrands(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "block"
        document.getElementById("customer_container").style.display = "none"
      }

      function toCustomerSupport(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "block"
      }

      function toLogin(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
        document.getElementById("login_container").style.display = "block"
      }

      function toSearch(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
        document.getElementById("search_container").style.display = "block"
      }

    return (
        <Fragment>
            <div id="brands_container">
                <style>{'body { background-color: grey; }'}</style>
                <header id="headerHome" className="text-center">
                    <nav className="navbar navbar-expand-lg navbar-light bg-dark subtle mb-4">
                        <div className="container-fluid">
                            <a className="navbar-brand text-light">SmartShopper</a>
                            <button onClick={toHome} className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                <span className="navbar-toggler-icon"></span>
                            </button>
                            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav me-auto mb-2 mb-lg-0" id="navbaritems">
                                <li className="nav-item">
                                    <button className="nav-link nav-item-link" aria-current="page" onClick={toHome}>Home</button>
                                </li>
                                <li className="nav-item">
                                    <button className="nav-link nav-item-link" onClick={toAboutUs}>About Us</button>
                                </li>
                                <li className="nav-item">
                                    <button className="nav-link active text-light" onClick={toBrands}>Brands</button>
                                </li>
                                <li className="nav-item">
                                    <button className="nav-link nav-item-link" onClick={toCustomerSupport}>Chatbot Customer Support</button>
                                </li>
                            </ul>
                                <form className="d-flex" action="/search" method="POST">
                                    <button className="btn btn-outline-secondary bg-info" type="submit" id="button-addon1"> 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16"> 
                                            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
                                        </svg>
                                    </button>
                                    <input className="form-control me-2" type="search" name="searchbar" placeholder="What are you looking for today..." aria-label="Search" style={{ minWidth: '800px' }} />
                                </form>
                                <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                                    <ul className="navbar-nav ms-auto">
                                        <li className="nav-item dropdown">
                                            <button type="button" class="btn btn-info" onClick={toLogin}>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                                            </svg> Login</button>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </nav>
                </header>
                <div id="brands_body">
                    <div class="card">
                        <h1>Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis eum similique ipsa reprehenderit voluptas voluptate sint harum. Necessitatibus tempora tempore neque omnis similique, quos nihil soluta aliquam, voluptas quod ipsum?</h1>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default Brands