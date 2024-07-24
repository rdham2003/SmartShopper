import React, { useEffect } from 'react'

function SignUp(){

    function switchSignLog(){
        document.getElementById("login_container").style.display = "block"
        document.getElementById("signup_container").style.display = "none"
    }

    return (
        <div id="signup_container" className="container mt-4">
            <div className="card text-center">
                <div className="card-body">
                    <h1 className="card-title">Sign Up Page</h1>
                    <br />
                    <br />
                    <br />     
                    <form>
                        <div className="mb-3">
                        <div className="form-floating mb-3">
                            <input type="text" className="form-control" id="floatingInput" placeholder="name@example.com" name="age"/>
                            <label htmlFor="floatingInput">Email</label>
                        </div>
                            <div id="emailHelp" className="form-text">
                                We'll never share your email with anyone else.
                            </div>
                        </div>
                        <div className="form-floating mb-3">
                            <input type="password" className="form-control" id="floatingInput" placeholder="name@example.com" name="age"/>
                            <label htmlFor="floatingInput">Password</label>
                        </div>
                        <div id="emailHelp" className="form-text">
                                We'll never share your password with anyone else.
                            </div>
                        <br />
                        <button type="submit" className="btn btn-primary">
                            Sign Up
                        </button>
                    </form>
                </div>
                <br />
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
    )
}

export default SignUp