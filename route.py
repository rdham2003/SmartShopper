from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
from backend.functions import highestRated, hotDeals

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')
CORS(app)

@app.route('/')
def serve():
    full_path = os.path.join(app.static_folder, 'index.html')
    print(full_path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_info():
    data = {
        "Deals": hotDeals(),
        "Rated": highestRated()
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
    return send_from_directory(app.static_folder, 'index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
