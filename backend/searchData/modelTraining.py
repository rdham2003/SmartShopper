import numpy as np
import pandas as pd
import torch 
import torch.nn as nn
from NN import NeuralNetwork
from torch.utils.data import Dataset, DataLoader
from NLP import tokenize, stemming, bag_of_words
import json

#Data Preprocessing
with(open("datasets/intentsSearch.json", 'r')) as intent:
    intents = json.load(intent)
    
all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        words = tokenize(pattern)
        all_words.extend(words)
        xy.append((words, tag))
        
ignore_words = ['?', '!', ',', '.']
all_words = [stemming(word) for word in all_words if word not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))
        
# print(all_words)
# print('\n')
# print(tags)
# print('\n')
# print(xy)

X_train = []
Y_train = []

for (strtok, tag) in xy:
    bag = bag_of_words(strtok, all_words)
    X_train.append(bag)
    
    label = tags.index(tag)
    Y_train.append(label)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_Data = X_train
        self.y_Data = Y_train
    
    def __getitem__(self, idx):
        return self.x_Data[idx], self.y_Data[idx]
    
    def __len__(self):
        return self.n_samples

#Hyperparameters
batch_size = 16
hidden_size = 150
input_size = len(all_words)
output_size = len(tags)
learning_rate = 0.0005
num_epochs = 1000
device = torch.device("cpu")

print(input_size, output_size)
dataset = ChatDataset()
train_loader = DataLoader(batch_size=batch_size, dataset=dataset, shuffle=True)
searchModel = NeuralNetwork(input_size=input_size, hidden_size=hidden_size, output_size=output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(searchModel.parameters(), lr=learning_rate)

#Model Training
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device, dtype=torch.float)
        labels = labels.to(device, dtype=torch.long)
        
        outputs = searchModel(words)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch + 1) % 50 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.5f}')
        
#Saving the Model
data = {
    "model_state": searchModel.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

torch.save(data, 'searchModel.pth')
print("Training complete")
        
        