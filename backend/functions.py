import random
import pickle
import numpy as np
import sqlite3
import pandas as pd
import torch
import json
from backend.searchData.NN import NeuralNetwork
from backend.searchData.NLP import tokenize, stemming, bag_of_words
from backend.ChatbotData.NN import NeuralNetwork2
import smtplib


surveyModel = pickle.load(open("model.pkl", "rb"))

with(open('datasets/intentsSearch.json')) as intent:
    intents = json.load(intent)
    
data = torch.load("searchModel.pth")

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

sermodel = NeuralNetwork(input_size, hidden_size, output_size).to(torch.device('cpu'))
sermodel.load_state_dict(model_state)
sermodel.eval()

with(open('datasets/intentsChatbot.json')) as intent2:
    intentsChatbot = json.load(intent2)
    
chatData = torch.load("chatbotModel.pth")

input_sizeChat = chatData["input_sizeChat"]
hidden_sizeChat = chatData["hidden_sizeChat"]
output_sizeChat = chatData["output_sizeChat"]
all_wordsChat = chatData["all_wordsChat"]
tagsChat = chatData["tagsChat"]
model_stateChat = chatData["model_stateChat"]

Chatmodel = NeuralNetwork2(input_sizeChat, hidden_sizeChat, output_sizeChat).to(torch.device('cpu'))
Chatmodel.load_state_dict(model_stateChat)
Chatmodel.eval()


def highestRated():
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
        prodList = sorted(prodList, key=lambda x: x[2])[::-1][:10]
        newProdList = []
        for prod in prodList:
            newProdList.append(prod[:3])
        return newProdList
    
def hotDeals():
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
    newProdList = []
    for i in range(10):
        newProdList.append(prodList[random.randint(0,199)][:3])
    return newProdList
        
def recommendProd(survArr):
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        prods = []
        prod_tags = []
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
            prods.append(prodList[i][:3])
            prod_tags.append(prodList[i][3:11])
        print(prods)
        print(prod_tags)
    clustered_tags = {
        'Gaming': ["Mouse", "Computing", "LED Display", "Smartwatch", "Headset", "Digital", "WiFi", "USB", "Camera", "Thermometer", "Bluetooth", "WiFi Extender", "Tablets", "Smartphones", "Devices", "HD Video", "VR", "PC Gaming", "Virtual Reality", "In-Ear", "Over-Ear", "Gaming", "Console", "Laptop", "Router", "RGB", "Video", "Immersive", "Gaming Experience", "Gaming Community"],
        'TV': ["Home Theater", "Projector", "Touchscreen"],
        'Music': ["Audio", "Speaker", "Earbuds", "Headphones", "Portable", "Over-Ear", "In-Ear", "Wireless", "Music", "Bluetooth", "Noise Cancelling"],
        'Home': ["Air Purifier", "Home Theater", "Appliances", "Ceiling Fan", "Vacuum", "Smoke Detector", "Bedroom", "Doorbell", "Garage Door Opener", "Door Lock", "Keyless", "Photo Frame", "Blanket", "Heating", "Cooling", "Thermostat", "Portable", "Compact", "Cleaning", "Storage", "Furniture", "Smart Home", "Home Gym", "Mattress", "Dimmable", "Rugged", "Tools", "Secure", "Shelter", "Home", "Comfort"],
        'Kitchen': ["Kettle", "Espresso", "Purification", "Bottle", "Cooking", "Coffee Maker", "Blender", "Hand Mixer", "Grilling", "Baking", "Cookware", "Pots and Pans", "Instant Pot", "Multi-Cooker", "Pressure Cooker", "Crockpot", "Coffee Grinder", "Food Preparation", "Drinkware", "Utensils", "Non-Stick", "Slow-Cooking", "Kitchen", "Barista", "Culinary", "Recipes", "Meals"],
        'Fitness': ["Hydration", "Weightlifting", "Exercise", "Running", "Workout", "Walking", "Cardio", "Biking", "Cycling", "Yoga", "Stretching", "Weights", "Fitness", "Athletics", "Sports", "Activewear", "Strength", "Performance", "Agility", "Mobility", "Training", "Fitness Tracker", "Endurance", "Body Composition", "Heart Rate", "Hydration Tracker", "Jump Rope", "Muscle", "Gym"],
        'Fashion': ["Clothing", "Footwear", "Accessories", "Eyewear", "Fashion", "Beachwear", "Leggings", "Shoes", "Boots", "Shaver", "Hair Dryer", "Hair Straightener", "Grooming", "Grooming Tools", "Stylish", "Trendy", "Casual", "Professional", "Lifestyle", "Outerwear", "Gloves", "Beachwear", "Leggings"],
        'Outdoors': ["Trekking", "Backpacking", "Climbing", "Hiking", "Camping", "Snowboarding", "Hammocking", "Rock Climbing", "Mountaineering", "Winter", "Outdoor", "Beach", "Adventure", "Survival", "Gear", "Lantern", "Helmet", "Rainwear", "Insulation", "Camping Gear", "Backpack", "Towel", "UV Protection"],
        'Personal Care': ["Oral Care", "Shaving", "Brushing", "Dental Care", "Personal Care", "Grooming", "Grooming Tools", "Hygiene", "Health", "Clean Air", "Sleep", "Relaxation", "Massage", "Comfortable"],
        'Utilities': ["Large", "Equipment", "Stability", "Capture", "Images", "Drinks", "Cafe", "Healthy Eating", "Study", "Leak Proof", "Bag", "Backpack", "Soft", "Warmth", "Comfortable", "Waterproof", "Lightweight", "Durable", "Insulated", "Stainless Steel", "Green", "Blue", "Gray", "White", "Black", "Ergonomic", "Adjustable", "Leak Proof", "Easy to Clean", "Portable", "Handheld", "Fast Charging", "Rechargeable", "Battery Operated", "Multi-Use", "Utility", "Convenience", "Secure", "Non-Slip", "Fast Boil", "Energy Efficient", "Solar Power", "HEPA Filter", "Electric", "High Speed", "WiFi Plug", "Smart", "Smart Home", "Smartwatch", "Noise Cancelling"]
    }
    surveyTags = list(clustered_tags.keys())
    survArr = np.array(survArr).reshape(1, -1)
    modelPred = surveyModel.predict(survArr)[0]
    rec_tags = []
    for i in range(len(surveyTags)):
        if modelPred[i] == 1:
            rec_tags.append(surveyTags[i])
    recProdList = []
    for i in range(len(rec_tags)):
        for j in range(len(clustered_tags[rec_tags[i]])):
            for k in range(len(prod_tags)):
                if clustered_tags[rec_tags[i]][j] in prod_tags[k]:
                    recProdList.append(prods[k])
                    prods.remove(prods[k])
                    prod_tags.remove(prod_tags[k])
                    break
    finalProdList = []
    for i in range(10):
        prodKey = random.randint(0, len(recProdList)-1)
        finalProdList.append(recProdList[prodKey])
        recProdList.remove(recProdList[prodKey])
    # print(finalProdList)
    return finalProdList

def get_response(product, prods, prod_tags):
    prod_search = []
    rec_prods = []
    
    text = product
    product = tokenize(product)
    bag = bag_of_words(product, all_words)
    bag = bag.reshape(1, bag.shape[0])
    bag = torch.from_numpy(bag).float()
    
    output = sermodel(bag)
    
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim=1)
    probability = probs[0][predicted.item()]
    
    print(probability.item())
    print(tag)
    
    if probability.item() >= 0.5:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                search_tags = intent["patterns"]
                for i in range(len(prods)):
                    for j in range(len(prod_tags[i])):
                        # print(prod_tags[i])
                        if prod_tags[i][j] in search_tags:
                            prod_search.append(prods[i])
                            break
    return prod_search
                
    
def productSearch(product):
    prods = []
    prod_tags = []
    search_results = []
    
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
            prods.append(prod[:3])
            prod_tags.append(prod[3:11])
    # return get_response(product, prods, prod_tags)
    # print(prods)
    # print('\n')
    # print(prod_tags)
    # print(len(prodList))
    for i in range(len(prodList)):
        # print(prods[i][0])
        # print('\n')
        # print(prod_tags[i])
        if product in prods[i][0] or product in prod_tags[i][3:11]:
            search_results.append(prods[i])
    if search_results == []:
        print("No close matches, but you may be interested in the following:")
        return get_response(product, prods, prod_tags)
    else:
        return search_results
    

def createUserDB():
    userDB = sqlite3.connect("database/userDB.db")
    userCur = userDB.cursor()
    
    with(open('database/createUserDB.sql', 'r')) as query:
        sql_query = query.read()
        
        userCur.execute(sql_query)
        
    userDB.commit()

    df = pd.read_sql_query('SELECT * FROM user_database', userDB)
    userDB.close()
    
    print(df.head())

def send_email(subject, body, receiver_email):
    sender_email = "twofactfactor@gmail.com"
    password = "gvhr hoxe ugcn gxcj"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    message = f"Subject: {subject}\n\n{body}"

    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)
    print("Email Sent")

def genCode():
    code = []
    for i in range(6):
        code.append(str(random.randint(0,9)))
        print(code)
    return ''.join(code)

def chatBotConvo(message):
    text = message
    message = tokenize(message)
    bag = bag_of_words(message, all_words)
    bag = bag.reshape(1, bag.shape[0])
    bag = torch.from_numpy(bag).float()
    
    output = Chatmodel(bag)
    
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim=1)
    probability = probs[0][predicted.item()]
    
    print(probability.item())
    print(tag)
    
    if probability.item() >= 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = f'{random.choice(intent["responses"])}'
    
    return response
    
if __name__ == '__main__':
    # print(highestRated())
    # print(hotDeals())
    # print(recommendProd([21, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]))
    # print(productSearch("Clothes"))
    # createUserDB()
    print(genCode())
    