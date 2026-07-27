import pandas as pd
df=pd.read_csv("MOCK_DATA.csv")
print(df)
print(df.head()) # Print the first 5 rows
print(df.tail()) # Print the last 5 rows
print(df.shape) # Print the number of rows and columns
df=pd.read_excel("MOCK_DATA.xlsx")
print(df)
s=pd.DataFrame(["Thala","100"])
print(s)
print()
print(df.to_csv("new score.csv",index=False))
print()

data = {'Name': ['Alice','Bob','Charlie','Diana'],
        'Age':  [25, 30, 22, 28],
        'City': ['Delhi','Mumbai','Pune','Chennai'],
        'Score':[88, 92, 75, 95]}
df = pd.DataFrame(data)

data = {'Name': ['Alice','Bob','Charlie','Diana'],
        'Age':  [25, 30, 22, 28],
        'Score':[88, 92, 75, 95]}
df = pd.DataFrame(data)

print(df.loc[0])  # Access the first row
print()
print(df.loc[0,'Name'])  # Access the 'Name' column of the first row
print()
print(df.loc[0:3, ['Name', 'Score']])  # Access rows 0 to 3 and columns 'Name' and 'Score'
print()
print(df.iloc[0])  # Access the first row using integer-based indexing
print()
print(df.iloc[0:3])  # Access rows 0 to 3 using integer-based indexing
print()
print(df.iloc[1:3, 0:2])  # Access rows 1 to 2 and columns 0 to 1 using integer-based indexinga


