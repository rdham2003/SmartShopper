import React, { useState, useEffect } from 'react';
import { Fragment } from 'react';

function AboutUs(props){

    console.log(`a;ofjakl;ghsg;jkh: ${props.isLoggedIn}`)
    console.log(`qa;gfa: ${props.userName}`)

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

      function toWishlist(){
        document.getElementById("homePage").style.display = "none"
        document.getElementById("aboutus_container").style.display = "none"
        document.getElementById("brands_container").style.display = "none"
        document.getElementById("customer_container").style.display = "none"
        document.getElementById("wishlist_container").style.display = "block"
    }

    console.log(`Bruhtha: ${props.isLoggedIn}`)

    useEffect(() => {
        if (props.isLoggedIn){
            document.getElementById("login_button").style.display = "none"
            document.getElementById("post_login").style.display = "block"
        }
        else {
            document.getElementById("login_button").style.display = "block"
            document.getElementById("post_login").style.display = "none"
        }
    });

    return (
        <Fragment>
            <div id="aboutus_container">
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
                                                </svg> Login</button>
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
                <div id="about_body">
                    <div class="card">
                        <h1>About Us</h1>
                        <br />
                        <h2>Welcome to SmartShopper!</h2>
                        <br />
                        <h4>At SmartShopper, we believe in leveraging the power of technology to enhance your shopping experience. Our platform is designed to understand your preferences and recommend products that fit your unique lifestyle. Whether you're a tech enthusiast, a fitness buff, a fashionista, or a home decor aficionado, SmartShopper has something special for you.</h4>
                        <br />
                        <hr />
                        <br />
                        <h1>Our Story</h1>
                        <br />
                        <h4>SmartShopper was born out of a passion for innovation and a desire to make online shopping more intuitive and enjoyable. Our founder, a Computer Science Junior at the University of Minnesota, combined expertise in artificial intelligence, machine learning, and web development to create a platform that anticipates your needs and helps you discover new products effortlessly.</h4>
                        <br />
                        <hr />
                        <br />
                        <h1>Our Technology</h1>
                        <br /> 
                        <h4>We utilize cutting-edge machine learning algorithms to analyze your interests and past purchases. Our hybrid recommendation system includes:</h4>
                        <ol>
                            <li><b>Interest-Based Recommendations:</b> A survey collects information about your hobbies and preferences, allowing our model to suggest items tailored to your tastes.</li>
                            <li><b>Search Recommendations:</b> The Neural Network Searchbar is an advanced search tool that uses neural networks to provide highly relevant search results. It goes beyond traditional keyword matching by understanding the context and intent behind user queries.</li>
                            <li><b>AI Chatbot Support:</b> The AI chatbot support system is designed to enhance user interaction and provide efficient solutions. It leverages natural language processing (NLP) and machine learning (ML) to understand and respond to user queries accurately.</li>
                        </ol>
                        <br />
                        <hr />
                        <br />
                        <h1>Our Mission</h1>
                        <br />
                        <h4>Our mission is to provide a seamless and personalized shopping experience. We aim to save you time and effort by bringing the products you love right to your fingertips. With SmartShopper, you can explore new items, find great deals, and enjoy a hassle-free shopping journey.</h4>
                        <br />
                        <hr />
                        <br />
                        <h1>Meet the Founder</h1>
                        <br />
                        <h4>Our founder is a dedicated student majoring in Computer Science and Business Management at the University of Minnesota. With a strong background in AI/ML and a passion for full-stack development, he has built SmartShopper to showcase the best of technology in e-commerce. He is constantly working to improve the platform and integrate new features that enhance user experience.</h4>
                        <br />
                        <hr />
                        <br />
                        <h1>Join Us</h1>
                        <br />
                        <h4>We are excited to have you as part of our community. Whether you're here to find your next favorite gadget or to explore new fashion trends, SmartShopper is here to make your shopping experience smarter and more enjoyable.</h4>
                        <br />
                        <h4>Thank you for choosing SmartShopper. Happy shopping!</h4>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default AboutUs