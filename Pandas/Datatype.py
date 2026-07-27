import pandas as pd

data = {'Name':  ['Alice', 'Bob', 'Charlie'],
        'Age':   ['25', '30', '22'],    
        'Score': ['88.5', '92.0', '75.5']}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)  #Check the data types of each column
print()
df['Age'] = df['Age'].astype(int)  #Convert the 'Age' column to integer type
print(df.dtypes)
print()
df['Score'] = df['Score'].astype(float)  
print(df.dtypes)







