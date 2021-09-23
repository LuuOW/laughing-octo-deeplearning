from sklearn.tree import export_graphviz
import graphviz as gv 
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from IPython.display import Image

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
feature_names = ['Pclass', 'male']
X = df[feature_names].values
y = df['Survived'].values

dt = DecisionTreeClassifier()
dt.fit(X, y)

dot_file = export_graphviz(dt, feature_names=feature_names)
graph = gv.Source(dot_file)
graph.render(filename='tree', format='png', cleanup=True)