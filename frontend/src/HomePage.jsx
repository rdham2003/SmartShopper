import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';
import Survey from './Survey';
import AboutUs from './AboutUs';
import Brands from './Brands.jsx';
import CustomerSupport from './CustomerSupport';
import LogIn from './LogIn'
import SignUp from './SignUp'
import Search from './Search'
import Wishlist from './Wishlist'

function HomePage(props) {

    const deals = [0.5,0.6,0.7,0.8]

    console.log(`Logged in?: ${props.isLoggedIn}`)
    console.log(`Username: ${props.userName}`)

    function takeSurvey(){
        document.getElementById("homePage").style.display = "none";
        document.getElementById("survey_container").style.display = "block"
      }
      
      function toSearch(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
        document.getElementById("search_container").style.display = "block"
      }

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

    //   console.log(`Survey products: ${props.survey}`)
    //   console.log(props.survey.length)
      
    //   function showSurvey(){
    //     if (props.survey.length === 0){
    //         document.getElementById("surv_container").style.display = "none"
    //         document.getElementById("preSurv_container").style.display = "block"
    //         console.log("Yes")
    //     }
    //     else{
    //         document.getElementById("surv_container").style.display = "inline-flex"
    //         document.getElementById("preSurv_container").style.display = "none"
    //         console.log("Naw")
    //     }
    // }

    useEffect(() => {
        if (props.survey.length === 0){
            document.getElementById("survey_title").style.display = "none"
            document.getElementById("recommend_container2").style.display = "none"
            document.getElementById("preSurv_container").style.display = "block"
        }
        else{
            document.getElementById("survey_title").style.display = "block"
            document.getElementById("recommend_container2").style.display = "inline-flex"
            document.getElementById("preSurv_container").style.display = "none"
        }
    }, [props.survey]);

    // console.log(`Search: ${props.searchOn}`)
    // console.log(document.getElementById("search_container").style.display)
    // console.log(`Sign in: ${props.signinErr}`)

    useEffect(() => {
        if (props.searchOn){
            document.getElementById("homePage").style.display = "none"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "block"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
        }
        else{
            document.getElementById("homePage").style.display = "block"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
        }
    }, [props.searchOn])

    useEffect(() => {
        if (props.incPass){
            document.getElementById("homePage").style.display = "none"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "block"
            document.getElementById("signup_container").style.display = "none"
        }
        else{
            document.getElementById("homePage").style.display = "block"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
        }
    }, [props.incPass])

    useEffect(() => {
        if (props.signinErr){
            document.getElementById("homePage").style.display = "none"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "block"
        }
        else{
            document.getElementById("homePage").style.display = "block"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
        }
    }, [props.signinErr])

    useEffect(() => {
        if (props.isLoggedIn){
            document.getElementById("login_button").style.display = "none"
            document.getElementById("post_login").style.display = "block"
        }
        else {
            document.getElementById("login_button").style.display = "block"
            document.getElementById("post_login").style.display = "none"
        }
    }, [props.isLoggedIn])

    useEffect(() => {
        if (props.onWishList){
            document.getElementById("homePage").style.display = "none"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "none"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
            document.getElementById("wishlist_container").style.display = "block"
        }
    })

    useEffect(() => {
        if (props.inCustomerSupport){
            document.getElementById("homePage").style.display = "none"
            document.getElementById("aboutus_container").style.display = "none"
            document.getElementById("brands_container").style.display = "none"
            document.getElementById("customer_container").style.display = "block"
            document.getElementById("search_container").style.display = "none"
            document.getElementById("login_container").style.display = "none"
            document.getElementById("signup_container").style.display = "none"
            document.getElementById("wishlist_container").style.display = "none"
        }
    })

    function toWishlist(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
        document.getElementById("wishlist_container").style.display = "block"
    }


    return (
        <Fragment>
            <style>{'body { background-color: grey; }'}</style>
            <div id="homePage" style={{ backgroundColor: 'grey' }}>
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
                                    <button className="nav-link active text-light" aria-current="page" onClick={toHome}>Home</button>
                                </li>
                                <li className="nav-item">
                                    <button className="nav-link nav-item-link" onClick={toAboutUs}>About Us</button>
                                </li>
                                <li className="nav-item">
                                    <button className="nav-link nav-item-link" onClick={toBrands}>Brands</button>
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
                                <div id='login_button'>
                                    <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                                        <ul className="navbar-nav ms-auto">
                                            <li className="nav-item dropdown">
                                                <button type="button" class="btn btn-info" onClick={toLogin}>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                                                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                                                </svg>Login</button>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div id='post_login'>
                                <nav className="navbar navbar-expand-lg navbar-light bg-dark subtle mb-4">
                                    <ul className="navbar-nav me-auto mb-2 mb-lg-0" id="navbaritems">
                                        <li className="nav-item">
                                            <button className="nav-link nav-item-link" onClick={toWishlist}>Wishlist</button>
                                        </li> 
                                        <li className="nav-item">
                                            <button className="nav-link nav-item-link">Welcome {props.userName}</button>
                                        </li>   
                                    </ul>
                                </nav>
                                </div>
                            </div>
                        </div>
                    </nav>
                </header>
                <div id="shopBody">
                    <div class="card">
                        <div id="preSurv_container">
                            <div class="card-body">
                                <div class="card">
                                    <div class="card-body">
                                        <h5 class="card-title">Click here to take a quick survey to recommend products most suited to your taste</h5>
                                        <button type="submit" class="btn btn-primary" onClick={takeSurvey}>Start survey</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <br />
                        <br />
                        <br />
                        <p class="fs-1" id='survey_title'>Based on your personal preferences 🧑</p>
                        <div id="recommend_container2">
                            {props.survey.map((item, index) => (
                                <div key={index} className="card" style={{ width: '18rem' }}>
                                    <form action="/wishlistadd" method="POST">
                                        <img src="..." className="card-img-top" alt="..." />
                                        <div className="card-body">
                                            <h5 className="card-title">{item[0]}</h5>
                                            <input type="hidden" name="prodName" value={item[0]} />
                                        </div>
                                        <ul className="list-group list-group-flush">
                                            <li className="list-group-item">${item[1]}</li>
                                            <input type="hidden" name="prodPrice" value={item[1]} />
                                            <li className="list-group-item">Rating: {item[2]} ⭐</li>
                                            <input type="hidden" name="prodRate" value={item[2]} />
                                        </ul>
                                        <div className="card-body">
                                            <button type="submit" className="btn btn-success">
                                                <small className="text-body-secondary">Add to wishlist</small>
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            ))}
                        </div>
                        <br />
                        <br />
                        <br />
                        <p class="fs-1">Highest Rated ⭐</p>
                        <div id="recommend_container">
                            {props.rated.map((item, index) => (
                                <div key={index} className="card" style={{ width: '18rem' }}>
                                    <form action="/wishlistadd" method="POST">
                                        <img src="..." className="card-img-top" alt="..." />
                                        <div className="card-body">
                                            <h5 className="card-title">{item[0]}</h5>
                                            <input type="hidden" name="prodName" value={item[0]} />
                                        </div>
                                        <ul className="list-group list-group-flush">
                                            <li className="list-group-item">${item[1]}</li>
                                            <input type="hidden" name="prodPrice" value={item[1]} />
                                            <li className="list-group-item">Rating: {item[2]} ⭐</li>
                                            <input type="hidden" name="prodRate" value={item[2]} />
                                        </ul>
                                        <div className="card-body">
                                            <button type="submit" className="btn btn-success">
                                                <small className="text-body-secondary">Add to wishlist</small>
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            ))}
                        </div>
                        <br />
                        <br />
                        <br />
                        <p class="fs-1">Hot Deals 🔥</p>
                        <div id="recommend_container">
                        {props.deals.map((item, index) => (
                            <div key={index} className="card" style={{ width: '18rem' }}>
                                <form action="/wishlistadd" method="POST">
                                    <img src="..." className="card-img-top" alt="..." />
                                    <div className="card-body">
                                        <h5 className="card-title">{item[0]}</h5>
                                        <input type="hidden" name="prodName" value={item[0]} />
                                    </div>
                                    <ul className="list-group list-group-flush">
                                        <li className="list-group-item">${item[1]}</li>
                                        <input type="hidden" name="prodPrice" value={item[1]} />
                                        <li className="list-group-item">Rating: {item[2]} ⭐</li>
                                        <input type="hidden" name="prodRate" value={item[2]} />
                                    </ul>
                                    <div className="card-body">
                                        <button type="submit" className="btn btn-success">
                                            <small className="text-body-secondary">Add to wishlist</small>
                                        </button>
                                    </div>
                                </form>
                            </div>
                        ))}
                        </div>
                    </div>
                </div>
            </div>
            <Survey />
            <AboutUs isLoggedIn={props.isLoggedIn} userName={props.userName}/>
            <Brands isLoggedIn={props.isLoggedIn} userName={props.userName}/>
            <CustomerSupport isLoggedIn={props.isLoggedIn} userName={props.userName} chats={props.chats}/>
            <LogIn incPass={props.incPass}/>
            <SignUp signinErr={props.signinErr}/>
            <Search search={props.search} isLoggedIn={props.isLoggedIn} userName={props.userName}/>
            <Wishlist isLoggedIn={props.isLoggedIn} userName={props.userName} wishList={props.wishList}/>
        </Fragment>
    );
}

export default HomePage;
