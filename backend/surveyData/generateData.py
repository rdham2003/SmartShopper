import numpy as np
import pandas as pd

tags = set()

df = pd.read_csv("datasets\products.csv")

df = df.drop(columns=["Name", "Price", "Review", "Shipping time"], axis=1)

# print(df.head())

data = {}
for column in df.columns:
    data[column] = df[column].tolist()

# print(data)

tag_data = data.keys()

for key in tag_data:
    for tag in data[key]:
        tags.add(tag)
        
tags.discard("3-5 days")
tags.discard("5-7 days")
# print(tags)

samples = 10000

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

survey = {
    'Age': np.random.randint(18,65,size=samples),
    'Gender_male': np.random.randint(0,2,size=samples),
    'Gender_female': np.random.randint(0,2,size=samples),
    'Traveling': np.random.randint(0,2,size=samples),
    'Reading': np.random.randint(0,2,size=samples),
    'FitnessFeat': np.random.randint(0,2,size=samples),
    'Cooking': np.random.randint(0,2,size=samples),
    'Arts & Crafts': np.random.randint(0,2,size=samples),
    'Movies & Shows': np.random.randint(0,2,size=samples),
    'GamingFeat': np.random.randint(0,2,size=samples),
    'OutdoorsFeat': np.random.randint(0,2,size=samples),
    'MusicFeat': np.random.randint(0,2,size=samples),
    'GamingVar': [],
    'TV': [],
    'MusicVar': [],
    'Home': [],
    'Kitchen': [],
    'FitnessVar': [],
    'Fashion': [],
    'OutdoorsVar': [],
    'Personal Care': [],
    'Utilities': []
}

gamingList = []
tvList = []
musicList = []
homeList = []
kitchenList = []
fitnessList = []
fashionList = []
outdoorsList = []
personalCareList = []
utilList = []

# print(survey)

for i in range(samples):
    gamingList.append(1) if (survey["Age"][i] >= 18 and survey["Age"][i] < 26) or (survey["GamingFeat"][i] == 1) else gamingList.append(0)
    musicList.append(1) if (survey["Age"][i] >= 18 and survey["Age"][i] < 26) or (survey["MusicFeat"][i] == 1) else musicList.append(0)   
    fashionList.append(1) if (survey["Age"][i] >= 18 and survey["Age"][i] < 26) or (survey["Arts & Crafts"][i] == 1) else fashionList.append(0) 
    fitnessList.append(1) if (survey["Age"][i] >= 18 and survey["Age"][i] < 26) or (survey["FitnessFeat"][i] == 1) else fitnessList.append(0)
    personalCareList.append(1) if (survey["Age"][i] >= 26 and survey["Age"][i] < 41) or (survey["Reading"][i] == 1) else personalCareList.append(0)
    utilList.append(1) if (survey["Age"][i] >= 26 and survey["Age"][i] < 41) or (survey["Age"][i] >= 56 and survey["Age"][i] < 66) or (survey["Arts & Crafts"][i] == 1) else utilList.append(0)
    kitchenList.append(1) if (survey["Age"][i] >= 26 and survey["Age"][i] < 41) or (survey["Cooking"][i] == 1) else kitchenList.append(0)
    homeList.append(1) if (survey["Age"][i] >= 41 and survey["Age"][i] < 56) or (survey["Age"][i] >= 56 and survey["Age"][i] < 66) else homeList.append(0)
    outdoorsList.append(1) if (survey["Age"][i] >= 41 and survey["Age"][i] < 56) or (survey["Traveling"][i] == 1) or (survey["OutdoorsFeat"][i] == 1) else outdoorsList.append(0)
    tvList.append(1) if (survey["Age"][i] >= 41 and survey["Age"][i] < 56) or (survey["Movies & Shows"][i] == 1) else tvList.append(0)

survey["GamingVar"] = gamingList
survey["TV"] = tvList
survey["MusicVar"] = musicList
survey["Home"] = homeList
survey["Kitchen"] = kitchenList
survey["FitnessVar"] = fitnessList
survey["Fashion"] = fashionList
survey["OutdoorsVar"] = outdoorsList
survey["Personal Care"] = personalCareList
survey["Utilities"] = utilList

surveyDF = pd.DataFrame(survey)

print(surveyDF.head())

surveyDF.to_csv('datasets/surveyData.csv', index=False)
print("Succesfully created training data")