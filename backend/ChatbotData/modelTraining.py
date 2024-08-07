import numpy as np
import pandas as pd
import torch 
import torch.nn as nn
from NN import NeuralNetwork2
from torch.utils.data import Dataset, DataLoader
from NLP import tokenize, stemming, bag_of_words
import json

#Data Preprocessing
with(open("datasets/intentsChatbot.json", 'r')) as intent:
    intents = json.load(intent)
    
# Data preprocessing
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

# Preparing training data
X_train = []
Y_train = []

for (tok_str, tag) in xy:
    bag = bag_of_words(tok_str, all_words)
    X_train.append(bag)
    
    label = tags.index(tag)
    Y_train.append(label)  

X_train = np.array(X_train)
Y_train = np.array(Y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train
    
    def __getitem__(self, idx):
        return self.x_data[idx], self.y_data[idx]
    
    def __len__(self):
        return self.n_samples

# Hyperparameters
batch_size = 8
hidden_size = 40
input_size = len(all_words)
output_size = len(tags)
learning_rate = 0.001
num_epochs = 500

print(input_size, output_size)

#Training the Model
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

device = torch.device('cpu')
model = NeuralNetwork2(input_size, hidden_size, output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device, dtype=torch.float)
        labels = labels.to(device, dtype=torch.long)

        outputs = model(words)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch + 1) % 50 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.5f}')

print(f'Final Loss: {loss.item():.5f}')
        
#Saving the Model
data = {
    "model_stateChat": model.state_dict(),
    "input_sizeChat": input_size,
    "output_sizeChat": output_size,
    "hidden_sizeChat": hidden_size,
    "all_wordsChat": all_words,
    "tagsChat": tags
}

torch.save(data, 'chatbotModel.pth')
print("Training complete")
        
        