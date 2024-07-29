from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
from backend.functions import highestRated, hotDeals, recommendProd, productSearch, get_response
import pickle
import numpy as np
import sqlite3

surveyModel = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')
CORS(app)

survey_results = []
search_results = []
searchOn = False

@app.route('/')
def serve():
    full_path = os.path.join(app.static_folder, 'index.html')
    print(full_path)
    
    global searchOn
    searchOn = False
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_info():
    data = {
        "Deals": hotDeals(),
        "Rated": highestRated(),
        "Survey": survey_results,
        "Search": search_results,
        "searchOn": searchOn
    }
    return jsonify(data)

@app.route('/survey', methods=["GET", "POST"])
def recommend():
    survey = []
    age = request.form.get("age")
    gender = request.form.get("gender")
    traveling = request.form.get("Traveling")
    reading = request.form.get("Reading")
    fitness = request.form.get("Fitness")
    cooking = request.form.get("Cooking")
    arts_crafts = request.form.get("Arts & Crafts")
    movie_tvshow = request.form.get("Watching Movies or TV Shows")
    gaming = request.form.get("Gaming")
    outdoors = request.form.get("Outdoor Activities")
    music = request.form.get("Music and Concerts")
    survey.append(int(age))
    if gender == 'male':
        survey.append(1)
        survey.append(0)
    else:
        survey.append(0)
        survey.append(1)
    survey.append(1) if traveling == 'on' else survey.append(0)
    survey.append(1) if reading == 'on' else survey.append(0)
    survey.append(1) if fitness == 'on' else survey.append(0)
    survey.append(1) if cooking == 'on' else survey.append(0)
    survey.append(1) if arts_crafts == 'on' else survey.append(0)
    survey.append(1) if movie_tvshow == 'on' else survey.append(0)
    survey.append(1) if gaming == 'on' else survey.append(0)
    survey.append(1) if outdoors == 'on' else survey.append(0)
    survey.append(1) if music == 'on' else survey.append(0)
    print(survey)
    print(age,gender,traveling,reading,fitness,cooking,arts_crafts,movie_tvshow,gaming,outdoors,music)
    survProds = recommendProd(survey)
    print(survProds)
    
    global survey_results
    survey_results = survProds
    
    global searchOn
    searchOn = False
    
    return send_from_directory(app.static_folder, 'index.html')
    
@app.route("/search", methods=["GET", "POST"])
def search():
    product = request.form.get("searchbar")
    search_prods = productSearch(product)
    print(search_prods)
    
    global search_results
    search_results = search_prods
    
    global searchOn
    searchOn = True
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form.get("username")
    email = request.form.get("email")
    phoneNo = request.form.get("phoneNumber")
    password = request.form.get("password")
    twofactor = request.form.get("twofactor")
    print(username, email, phoneNo, password, twofactor)
    
    userDB = sqlite3.connect("database/userDB.db")
    userCur = userDB.cursor()
    
    userCur.execute("SELECT * FROM user_database")
    users = userCur.fetchall()
    userDB.commit()
    
    print(users)
    
    for user in users:
        if (username in user) or (email in user):
            print("Username or email already in use")
    
    if(twofactor == "on"):
        return send_from_directory(app.static_folder, 'test.html')
    else:
        query = "INSERT INTO user_database (username, email, phoneNumber, password, twofactor) VALUES (?,?,?,?,?)"
        data = (username, email, phoneNo, password, twofactor)
        
        userCur.execute(query, data)
        userDB.commit()
        userDB.close()
        
        return send_from_directory(app.static_folder, "index.html")

@app.route("/twofactor", methods=["GET", "POST"])
def twofactor():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
    

