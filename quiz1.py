import numpy as np 
import pandas as pd

filename = input()
column_name = input()

#print the elements in the given column.
data = pd.read_csv(filename)
print(data[column_name].values)
