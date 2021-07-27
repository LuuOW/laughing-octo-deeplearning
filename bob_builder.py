import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.linear_model import LogisticRegression


n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

#build a Logistic Regression model with the feature matrix and make a prediction 1 or 0 of the single datapoint
model = LogisticRegression()
model.fit(X, y)
predict = model.predict([datapoint])
print(int(predict))

