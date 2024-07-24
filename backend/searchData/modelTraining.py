import numpy as np
import pandas as pd
import torch 
import torch.nn as nn
from NN import NeuralNetwork
from NLP import tokenize, stemming, bag_of_words

df = pd.read_csv("datasets/products.csv")

df = df.drop(["Price", "Review", "Shipping time"], axis=1)

print(df.head())