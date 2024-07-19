import numpy as np
import pandas as pd

tags = set()

df = pd.read_csv("E-commerce\datasets\products.csv")

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
print(tags)
