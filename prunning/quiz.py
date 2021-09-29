import numpy as np


targetValues = [int(x) for x in input().split()]
leftSplit = [int(x) for x in input().split()]
rightSplit = [int(x) for x in input().split()]

leftGini = 1 - np.sum(leftSplit) / np.sum(targetValues)**2
rightGini = 1 - np.sum(rightSplit) / np.sum(targetValues)**2
infoGain = np.sum(targetValues) / np.sum(targetValues)**2 - leftGini - rightGini
print(round(infoGain, 5))