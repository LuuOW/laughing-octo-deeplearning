from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import numpy as np

X, y = fetch_openml('mnist_784', version=1, return_X_y=True)


print(X.shape, y.shape)
print(np.min(X), np.max(X))
print(y[0:5])

X5 = X[y <= '3']
y5 = y[y <= '3']

mlp=MLPClassifier(
  hidden_layer_sizes=(6,), 
  max_iter=200, alpha=1e-4,
  solver='sgd', random_state=2)

mlp.fit(X5, y5)