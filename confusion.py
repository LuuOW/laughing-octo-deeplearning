import numpy as np

conf = [[20, 26], [10, 44]]
#calculate the accuracy of the conf matrix
acc = np.mean(np.diag(conf))
print(acc)