import React, { useEffect } from 'react';

function LogIn(props) {

    function switchLogSign(){
        document.getElementById("login_container").style.display = "none"
        document.getElementById("signup_container").style.display = "block"
    }

    function passDisplay(){
        if (document.getElementById("password1").type == "password"){
            document.getElementById("password1").type = "text";
        }
        else{
            document.getElementById("password1").type = "password";
        }
    }

    useEffect(() => {
        if (props.incPass){
            document.getElementById("error_login").style.display = "block"
        }
    })

    return (
        <div id="login_container" className="container mt-4">
            <div className="card text-center">
                <div className="card-body">
                    <h1 className="card-title">Login Page</h1>
                    <br />
                    <br />
                    <br />    
                    <h2 id="error_login" style={{color: "red"}}>Error: Incorrect username or password</h2> 
                    <form action='/login' method='POST'>
                        <div className="mb-3">
                        <div className="form-floating mb-3">
                            <input required type="text" className="form-control" id="floatingInput" placeholder="name@example.com" name="username"/>
                            <label htmlFor="floatingInput">Username</label>
                        </div>
                            <div id="emailHelp" className="form-text">
                                We'll never share your email with anyone else.
                            </div>
                        </div>
                        <div className="form-floating mb-3">
                            <input required type="password" id="password1" className="form-control" placeholder="name@example.com" name="password"/>
                            <label htmlFor="floatingInput">Password</label>
                        </div>
                        <div id="emailHelp" className="form-text">
                                We'll never share your password with anyone else.
                            </div>
                            <button onClick={passDisplay} type="button" class="btn btn-secondary">Show/Hide Password</button>
                            <br />
                        <br />
                        <button type="submit" className="btn btn-primary">
                            Log In
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
                    Don't have an account?
                    <br />
                    <button className="btn btn-primary" onClick={switchLogSign}>
                        Sign Up
                    </button>
                </div>
            </div>
        </div>
    );
}

export default LogIn;
