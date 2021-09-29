import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


random_state = int(input())
dataPoints = int(input())
rows = []
for i in range(dataPoints):
    rows.append([float(a) for a in input().split()])

featureMatrix = np.array(rows)
targetArray = np.array([int(a) for a in input().split()])

# Split the data into training and test sets using the random_state value, build a random forest 
# model with the training data, and predict the test data, use 5 trees.
X_train, X_test, y_train, y_test = train_test_split(featureMatrix, targetArray, random_state=random_state)
clf = RandomForestClassifier(n_estimators=5, random_state=random_state)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print (predictions)