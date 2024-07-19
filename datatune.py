import pandas as pd
import numpy as np
import random

samples = 100
shipping = ["3-5 days", "5-7 days"]
funny = []

for i in range(samples):
    funny.append(shipping[random.randint(0,1)])

df = pd.read_csv("E-commerce\datasets\products.csv")

df = df.drop(columns=["Img file path"], axis=1)

print(df.head())

df.to_csv("E-commerce\E-commerce\src\\assets\products.csv", index=False)