import numpy as np


w1, w2, b, x1, x2 = [float(x) for x in input().split()]


def sigmoid(x):
  return 1 / (1 + np.exp(-x))

print(round(sigmoid(w1 * x1 + w2 * x2 + b), 4))


