from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os

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
        "Deals": ["Name",29.99,4.6],
        "Rated": ["Name",29.99,4.6],
    }
    return jsonify(data)

@app.route('/survey', methods=["GET", "POST"])
def recommend():
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
    print(age,gender,traveling,reading,fitness,cooking,arts_crafts,movie_tvshow,gaming,outdoors,music)
    return "Form submitted successfully"
    

if __name__ == "__main__":
    app.run(debug=True)
