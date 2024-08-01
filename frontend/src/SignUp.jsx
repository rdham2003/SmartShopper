import React, { useState, useEffect } from 'react'
import { Fragment } from 'react';

function SignUp(props){

    const [pass, setPass] = useState("")

    function handleInputChange(event){
        setPass(event.target.value)
    }

    function passDisplay(){
        if (document.getElementById("password").type == "password"){
            document.getElementById("password").type = "text";
        }
        else{
            document.getElementById("password").type = "password";
        }
    }

    function genPass() {
        const lowerAlph = [...'abcdefghijklmnopqrstuvwxyz'];
        const upperAlph = [...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'];
        const numList = [...'0123456789'];
        const symbList = [...'!@#$%^&*'];
        
        let randPass = [];

        for (let i = 0; i < 16; i++){
            let getRand = Math.floor(Math.random() * 4);
            switch(getRand){
                case(0):
                    randPass.push(lowerAlph[Math.floor(Math.random() * lowerAlph.length)]);
                    break;
                case(1):
                    randPass.push(upperAlph[Math.floor(Math.random() * upperAlph.length)]);
                    break;
                case(2):
                    randPass.push(numList[Math.floor(Math.random() * numList.length)]);
                    break;
                case(3):
                    randPass.push(symbList[Math.floor(Math.random() * symbList.length)]);
                    break;
            }
        }
        console.log(randPass)
        setPass(randPass.join(''));
        document.getElementById("password").type = "text"
    }

    function switchSignLog(){
        document.getElementById("login_container").style.display = "block"
        document.getElementById("signup_container").style.display = "none"
    }

    useEffect(() => {
        if (props.signinErr){
            document.getElementById("signup_error").style.display = "block"
        }
    }, [props.signinErr])
    
    return (
        <Fragment>
            <div id="signup_container" className="container mt-4">
                <div className="card text-center">
                    <div className="card-body">
                        <h1 className="card-title">Sign Up Page</h1>
                        <br />
                        <br />
                        <br />     
                        <h2 id="signup_error" style={{color: "red"}}>Error: Username or email is already in use</h2>
                        <form action='/signup' method='POST'>
                            <div className="mb-3">
                            <div className="form-floating mb-3">
                                <input required name="username" type="text" className="form-control" id="floatingInput" placeholder="john.appleseed"/>
                                <label htmlFor="floatingInput">Username</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input required name="email" type="text" className="form-control" id="floatingInput" placeholder="jappleseed@example.com"/>
                                <label htmlFor="floatingInput">Email</label>
                            </div>
                            <div id="emailHelp" className="form-text">
                                We'll never share your email with anyone else.
                            </div>
                            <div className="form-floating mb-3">
                                <input required name="phoneNumber" type="tel" placeholder="123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" className="form-control" id="floatingInput"/>
                                <label htmlFor="floatingInput">Phone Number</label>
                            </div>
                            <div id="emailHelp" className="form-text">
                                Format: 123-456-7890
                            </div>
                            </div>
                            <div className="form-floating mb-3">
                                <input required name="password" type="password" value={pass} onChange={handleInputChange} className="form-control" id="password" placeholder="name@example.com"/>
                                <label htmlFor="floatingInput">Password</label>
                            </div>
                                <div class="d-grid gap-2 d-md-block">
                                    <button onClick={genPass} type="button" class="btn btn-secondary">Generate Strong Password</button>
                                    <button onClick={passDisplay} type="button" class="btn btn-secondary">Show/Hide Password</button>
                                </div>

                            <div id="emailHelp" className="form-text">
                                    We'll never share your password with anyone else.
                            </div>
                            <br />
                            <div id="two_container">
                                <div class="form-check form-switch">
                                    <input name="twofactor" class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault"/>
                                    <label class="form-check-label" for="flexSwitchCheckDefault">Enable Two-Factor Authentication</label>
                                </div>
                            </div>
                            <br />
                            <br />
                            <button type="submit" className="btn btn-primary">
                                Sign Up
                            </button>
                        </form>
                    </div>
                    <br />
                    <form action="/homepage" method='POST'>
                        <button class="btn btn-primary" type="submit">Go to homepage</button>
                    </form>
                    <br />
                    <br />
                    <div className="card-footer text-body-secondary">
                        Already have an account?
                        <br />
                        <button className="btn btn-primary" onClick={switchSignLog}>
                            Log In
                        </button>
                    </div>
                </div>
            </div>
            </Fragment>
    )
}

export default SignUp