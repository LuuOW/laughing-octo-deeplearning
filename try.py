import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'


y_pred = [0, 0, 1, 1, 0]
y = np.array([0,0,0,1,1])

print((y == y_pred).sum() / y.shape[0])
