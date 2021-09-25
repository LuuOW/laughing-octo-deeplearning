import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import entropy

S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

def gini(S, A, B):
    left = 0
    right = 0
    for i in range(len(S)):
        if S[i] in A:
            left += 1
        else:
            right += 1
    left = left / len(S)
    right = right / len(S)
    return round(1 - (left * left + right * right), 5)
print (gini(S, A, B))

