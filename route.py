from flask import Flask, jsonify, send_from_directory, request, session
from flask_cors import CORS
import os
from backend.functions import highestRated, hotDeals, recommendProd, productSearch, get_response, genCode, send_email, createUserDB, chatBotConvo
import pickle
import numpy as np
import sqlite3

surveyModel = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')
CORS(app)
app.secret_key = '252525'

survey_results = []
search_results = []
searchOn = False
incPass = False
signinErr = False
isLoggedIn = False
wishList = []
onWishList = False
userName = ''
chats = ["Hello! How can I help you today?"]
inCustomerSupport = False

@app.route('/')
def serve():
    full_path = os.path.join(app.static_folder, 'index.html')
    print(full_path)
    
    global searchOn
    searchOn = False
    
    global incPass
    incPass = False
    
    global signinErr
    signinErr = False
    
    global onWishList
    onWishList = False
    
    global inCustomerSupport
    inCustomerSupport = False
    
    createUserDB()
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_info():
    data = {
        "Deals": hotDeals(),
        "Rated": highestRated(),
        "Survey": survey_results,
        "Search": search_results,
        "searchOn": searchOn,
        "incPass": incPass,
        "signinErr": signinErr,
        "isLoggedIn": isLoggedIn,
        "userName": userName,
        "wishList": wishList,
        "onWishList": onWishList,
        "chats": chats,
        "inCustomerSupport": inCustomerSupport
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
    
    global incPass
    incPass = False
    
    global signinErr
    signinErr = False
    
    global inCustomerSupport
    inCustomerSupport = False
    
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
    
    global inCustomerSupport
    inCustomerSupport = False
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form.get("username")
    email = request.form.get("email")
    phoneNo = request.form.get("phoneNumber")
    password = request.form.get("password")
    twofactor = request.form.get("twofactor")
    print(username, email, phoneNo, password, twofactor)
    session['username'] = username
    session['email'] = email
    session['phoneNo'] = phoneNo
    session['password'] = password
    session['twofactor'] = twofactor
    
    userDB = sqlite3.connect("database/userDB.db")
    userCur = userDB.cursor()
    
    userCur.execute("SELECT * FROM user_database")
    users = userCur.fetchall()
    userDB.commit()
    
    print(users)
    
    global signinErr
    global userName
    global isLoggedIn
    global incPass
    
    global inCustomerSupport
    inCustomerSupport = False
    
    for user in users:
        if (username in user) or (email in user):
            print("Username or email already in use")
            signinErr = True
            return send_from_directory(app.static_folder, 'index.html')
    
    if(twofactor == "on"):
        print(f"database/{username}DB.db")
        newuserDB = sqlite3.connect(f"database/{username}DB.db")
        newuserCur = newuserDB.cursor()
        
        createWishList = f'''CREATE TABLE IF NOT EXISTS {username}_wishlist (
                            keyID INTEGER PRIMARY KEY AUTOINCREMENT,
                            product TEXT,
                            price FLOAT,
                            rating FLOAT
                            )'''
                                    
        newuserCur.execute(createWishList)
        newuserDB.commit()
        newuserDB.close()
        
        two_factor = genCode()
        session['two_factor'] = two_factor
        send_email("Two factor", f'{two_factor} is your authorization code', email)
        
        return send_from_directory(app.static_folder, 'twofact.html')
    else:
        query = "INSERT INTO user_database (username, email, phoneNumber, password, twofactor) VALUES (?,?,?,?,?)"
        data = (username, email, phoneNo, password, twofactor)
        
        userCur.execute(query, data)
        userDB.commit()
        userDB.close()
        
        newuserDB = sqlite3.connect(f"database/{username}DB.db")
        newuserCur = newuserDB.cursor()
        
        createWishList = f'''CREATE TABLE IF NOT EXISTS {username}_wishlist (
                            keyID INTEGER PRIMARY KEY AUTOINCREMENT,
                            product TEXT,
                            price FLOAT,
                            rating FLOAT
                            )'''
                                    
        newuserCur.execute(createWishList)
        newuserDB.commit()
        newuserDB.close()
        
        session.pop('username', None)
        session.pop('email', None)
        session.pop('phoneNo', None)
        session.pop('password', None)
        session.pop('twofactor', None)
        
        isLoggedIn = True
        userName = username
        incPass = False
        signinErr = False
        
        return send_from_directory(app.static_folder, "index.html")

@app.route("/twofactor", methods=["GET", "POST"])
def twofactor():
    userDB = sqlite3.connect("database/userDB.db")
    userCur = userDB.cursor()
    
    global incPass
    global signinErr
    global isLoggedIn
    global userName
    
    global inCustomerSupport
    inCustomerSupport = False
    
    twofact = request.form.get("twofact", '').strip()
    two_factor = str(session.get('two_factor', '')).strip()
    
    if two_factor == twofact:
        username = session.get('username', '').strip()
        email = session.get('email', '').strip()
        phoneNo = session.get('phoneNo', '').strip()
        password = session.get('password', '').strip()
        twofactor = session.get('twofactor', '').strip()
        
        query = "INSERT INTO user_database (username, email, phoneNumber, password, twofactor) VALUES (?,?,?,?,?)"
        data = (username, email, phoneNo, password, twofactor)
        userCur.execute(query, data)
        userDB.commit()
        userDB.close()
        
        session.pop('username', None)
        session.pop('email', None)
        session.pop('phoneNo', None)
        session.pop('password', None)
        session.pop('twofactor', None)
        session.pop('two_factor', None)
        
        incPass = False
        signinErr = False
        isLoggedIn = True
        userName = username
        
        return send_from_directory(app.static_folder, 'index.html')
    else:
        incPass = False
        signinErr = False
        isLoggedIn = True
        return send_from_directory(app.static_folder, 'twofacterror.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    userDB = sqlite3.connect("database/userDB.db")
    userCur = userDB.cursor()
    
    userCur.execute("SELECT * FROM user_database")
    users = userCur.fetchall()
    
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()
    
    global incPass
    global isLoggedIn
    global userName
    global wishList
    
    global inCustomerSupport
    inCustomerSupport = False
    
    for user in users:
        print(user[1], user[2])
        if user[1] == username and user[2] == password:
            if user[5] == 'on':
                two_factor = genCode()
                session['two_factor'] = two_factor
                send_email("Two factor", f'{two_factor} is your authorization code', user[3])
                return send_from_directory(app.static_folder, 'twofact.html')
            else:
                userDB.close()
                incPass = False
                isLoggedIn = True
                userName = username
                
                wishDB = f'database/{userName}DB.db'
                user_wishDB = sqlite3.connect(wishDB)
                user_wishCur = user_wishDB.cursor()
                
                user_wishCur.execute(f"SELECT * from {userName}_wishlist")
                user_wish = user_wishCur.fetchall()
                user_wishDB.commit()
                
                wishList = user_wish
                
                return send_from_directory(app.static_folder, 'index.html')
    
    userDB.close()
    print("Username or password incorrect")
    incPass = True
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/homepage', methods=["GET", "POST"])
def homepageroute():
    global incPass
    global signinErr
    global onWishList
    
    incPass = False
    signinErr = False
    onWishList = False
    
    global inCustomerSupport
    inCustomerSupport = False
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/wishlistadd', methods=["GET", "POST"])
def add_to_wishlist():
    name = request.form.get("prodName")
    price = request.form.get("prodPrice")
    rating = request.form.get("prodRate")
    # item = [name, price, rating]
    # print(item)
    # global wishList
    # wishList.append(item)
    global userName
    global wishList
    
    global inCustomerSupport
    inCustomerSupport = False
    
    if userName != '':
        wishDB = f'database/{userName}DB.db'
        user_wishDB = sqlite3.connect(wishDB)
        user_wishCur = user_wishDB.cursor()
        query = f"INSERT INTO {userName}_wishlist (product, price, rating) VALUES (?,?,?)"
        data = (name, price, rating)
        print(data)
        user_wishCur.execute(query, data)
        
        user_wishCur.execute(f"SELECT * from {userName}_wishlist")
        user_wish = user_wishCur.fetchall()
        user_wishDB.commit()
        
        print(user_wish)
        wishList = user_wish
        
        user_wishDB.commit()
        user_wishDB.close()
            
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/deletewish', methods=["GET", "POST"])
def delete_from_wishlist():
    global onWishList
    global wishList
    onWishList = True
    
    global inCustomerSupport
    inCustomerSupport = False
    
    prodName = request.form.get("product_name")
    print(prodName)
    
    wishDB = f'database/{userName}DB.db'
    user_wishDB = sqlite3.connect(wishDB)
    user_wishCur = user_wishDB.cursor()
    
    user_wishCur.execute(f"SELECT * from {userName}_wishlist")
    user_wish = user_wishCur.fetchall()
    print(user_wish)
    
    query = f"DELETE FROM {userName}_wishList WHERE product= ?"
    
    user_wishCur.execute(query, (prodName,))
    
    user_wishCur.execute(f"SELECT * from {userName}_wishlist")
    user_wish = user_wishCur.fetchall()
    user_wishDB.commit()
    
    print(user_wish)
    wishList = user_wish
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/ChatbotConvo", methods=["GET", "POST"])
def chatbotresponse():
    global chats
    global inCustomerSupport
    
    question = request.form.get("chatbot_prompt")
    chats.append(question)
    print(chats)
    chats.append(chatBotConvo(question))
    inCustomerSupport = True
    
    return send_from_directory(app.static_folder, 'index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    

