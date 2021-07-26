import pandas as pd
#pd.options.display.max_columns = 6
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
col = df['Fare']
print(col)
#print(df.describe())
