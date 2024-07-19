import React, { useState } from 'react'

function Survey() {
    const [checked, setChecked] = useState(0);
    
    const survey = ["Traveling", "Reading", "Fitness", "Cooking", "Arts & Crafts", "Watching Movies or TV Shows", "Gaming", "Outdoor Activities", "Music and Concerts"];
    
    function addChecked(event) {
        console.log(checked)
        event.target.checked ? (checked < 3 ? setChecked(checked+1) : event.preventDefault()) : setChecked(checked-1)
    }

    return (
        <form action="/survey" method="POST">
            <div id="survey_container">
                <div className="card text-center">
                    <div className="card-header">
                        Featured
                    </div>
                    <div className="card-body">
                        <h1>Personal Survey</h1>
                        <br /><br /><br />
                        <div className="form-floating mb-3">
                            <input type="number" className="form-control" id="floatingInput" placeholder="name@example.com" name="age"/>
                            <label htmlFor="floatingInput">Age</label>
                        </div>
                        <br />
                        <h4>Gender?</h4>
                        <div className="input-group mb-3">
                            <div className="input-group-text">
                                <input  className="form-check-input mt-0" type="radio" name="gender" value="male" id="male"/>
                            </div>
                            <label className="form-control" htmlFor="male">Male</label>
                        </div>
                        <div className="input-group mb-3">
                            <div className="input-group-text">
                                <input className="form-check-input mt-0" type="radio" name="gender" value="female" id="female"/>
                            </div>
                            <label className="form-control" htmlFor="female">Female</label>
                        </div>
                        <br />
                        <h4>What types of activities do you enjoy in your free time? (Select up to 3)</h4>
                        {survey.map((survey) =>
                            <div className="input-group mb-3">
                                <div className="input-group-text">
                                    <input className="form-check-input mt-0" type="checkbox" id={survey} name={survey} onClick={addChecked} disabled={checked === 3 && !document.getElementById(survey).checked}/>
                                </div>
                                <label className="form-control" htmlFor={survey}>{survey}</label>
                            </div>
                        )}
                        <br /><br /><br />
                        <button type="button" class="btn btn-primary">Submit</button>
                    </div>
                    <div className="card-footer text-muted">
                        2 days ago
                    </div>
                </div>
            </div>
        </form>
    );
}

export default Survey;
