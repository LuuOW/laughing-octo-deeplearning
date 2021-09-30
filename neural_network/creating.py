from sklearn.datasets import make_classification
from matplotlib import pyplot as plt

X, y = make_classification(n_features=3, n_redundant=1, n_informative=2)
print (X)
print (y)

#correct shape for X and y
print (X.shape)
print (y.shape)