import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, hamming_loss, jaccard_score, classification_report
import pickle

df = pd.read_csv("datasets\surveyData.csv")
print(df.head())

X = df[["Age", "Gender_male", "Gender_female", "Traveling","Reading","FitnessFeat","Cooking","Arts & Crafts","Movies & Shows","GamingFeat","OutdoorsFeat","MusicFeat"]]
Y = df.drop(["Age", "Gender_male", "Gender_female", "Traveling","Reading","FitnessFeat","Cooking","Arts & Crafts","Movies & Shows","GamingFeat","OutdoorsFeat","MusicFeat"], axis=1)

print(X,Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

surveyModel = MultiOutputClassifier(RandomForestClassifier(n_estimators=1500, max_depth=4, random_state=1))
surveyModel.fit(X,Y)

Y_pred = surveyModel.predict(X_test)

precision = precision_score(Y_test, Y_pred, average='macro', zero_division=1)
recall = recall_score(Y_test, Y_pred, average='macro', zero_division=1)
f1 = f1_score(Y_test, Y_pred, average='macro', zero_division=1)
classReport = classification_report(Y_test, Y_pred)
hammingLoss = hamming_loss(Y_test, Y_pred)
jaccard = jaccard_score(Y_test, Y_pred, average='macro')

print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1:.4f}')
print(f'Classification Report: \n{classReport}')
print(f'Hamming Loss: {hammingLoss:.4f}')
print(f'Jaccard Score: {jaccard:.4f}')

# Precision: 0.9765
# Recall: 1.0000
# F1 Score: 0.9879
# Classification Report:
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00      1581
#            1       1.00      1.00      1.00      1349
#            2       1.00      1.00      1.00      1161
#            3       1.00      1.00      1.00      1529
#            4       0.95      1.00      0.98      1663
#            5       1.00      1.00      1.00      1591
#            6       1.00      1.00      1.00      1136
#            7       0.95      1.00      0.97      1644
#            8       0.96      1.00      0.98      1658
#            9       0.91      1.00      0.95      1511

#    micro avg       0.97      1.00      0.99     14823
#    macro avg       0.98      1.00      0.99     14823
# weighted avg       0.97      1.00      0.99     14823
#  samples avg       0.98      1.00      0.99     14823

# Hamming Loss: 0.0200
# Jaccard Score: 0.9765

test = np.array([19,1,1,1,1,1,1,1,0,0,1,0]).reshape(1,-1)
print(test)

modelOutput = surveyModel.predict(test)
print(modelOutput)

with open("model.pkl", 'wb') as model_file:
    pickle.dump(surveyModel, model_file)
    print("Succesfully trained and saved model")
