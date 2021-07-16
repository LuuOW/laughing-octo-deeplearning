import numpy as np

ages = [15, 16, 18, 19, 22, 24, 29, 30, 34]

#mean of ages
mean = np.mean(ages)

#how far is heach value from mean
dev = ages - mean

print(dev)

#standard deviation of ages
std = np.std(ages)

#variance of ages
variance = np.var(ages)
print (variance)