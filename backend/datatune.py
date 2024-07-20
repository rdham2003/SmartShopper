import pandas as pd
import numpy as np
import random

samples = 200
# shipping = ["3-5 days", "5-7 days"]
# funny = []

# for i in range(samples):
#     funny.append(shipping[random.randint(0,1)])

df = pd.read_csv("datasets\products.csv")

df = df.drop(columns=["Review"], axis=1)
df.insert(2, "Review", np.round(np.random.uniform(3.5,5.0, size=samples),1))

print(df.head())

df.to_csv("datasets\products.csv", index=False)