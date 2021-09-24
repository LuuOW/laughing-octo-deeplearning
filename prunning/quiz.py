import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

def gini_impurity(S, A, B):
    p_A = len(A)/(len(A)+len(B))
    p_B = len(B)/(len(A)+len(B))
    gini = 1 - (p_A**2 + p_B**2)
    return gini

print (gini_impurity(S, A, B))