import pandas as pd
import numpy as np

data = {'Name':  ['Alice', 'Bob', None,    'Diana'],
        'Age':   [25,       None,  22,      28],
        'Score': [88,       92,    75,      None]}
df = pd.DataFrame(data)

print(df)
print()
print(df.isnull())  # Check for missing values
print()
print(df.isnull().sum())  # Count missing values in each column
print()
print(df.dropna())  # Drop rows with any missing values
print()


data = {'Name':  ['Alice', 'Bob',   'Charlie', 'Diana'],
        'Age':   [25,       np.nan,  22,         28],
        'Score': [88,       92,      np.nan,     95]}
df = pd.DataFrame(data)

print(df)
print()
average_age=df['Age'].mean()
print(average_age)  # Calculate the average age, ignoring NaN values
print()
print(df.fillna({'Age': average_age}))  # Fill missing values with specified values
print()
df['Score'] = df['Score'].fillna(100)  # Fill missing values in the 'Score' column with 33
print(df)

