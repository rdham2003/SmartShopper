from flask import Flask, jsonify, send_from_directory, request
import os

app = Flask(__name__, static_folder='frontend', static_url_path='/')

@app.route('/')
def serve():
    full_path = os.path.join(app.static_folder, 'index.html')
    print(full_path)
    return send_from_directory(app.static_folder, 'index.html')

def get_info():
    info = {
        "members": ["Member1", "Member2", "Member3"]
    }
    return jsonify(info)

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
