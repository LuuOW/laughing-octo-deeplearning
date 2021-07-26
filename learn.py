import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

ages = [15, 16, 18, 19, 22, 24, 29, 30, 34]


sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

#print 60% of ages
print (np.percentile(ages, 60))

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

#dataframe of titanic.csv 
titanic = pd.read_csv('titanic.csv')
