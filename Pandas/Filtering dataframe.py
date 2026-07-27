import pandas as pd

data = {'Name': ['Alice','Bob','Charlie','Diana','Ethan'],
        'Age':  [25, 30, 22, 28, 21],
        'City': ['Delhi','Mumbai','Pune','Delhi','Chennai'],
        'Score':[88, 92, 75, 95, 80]}
df = pd.DataFrame(data)

print(df[df['Age'] > 25])  # Filter rows where Age is greater than 25
print()
print(df[df['City']=="Delhi"])  # Filter rows where City is Delhi
print()
print(df[(df['Age']>25) & (df['City']=="Delhi")])  # Filter rows where Age is greater than 25 and City is Delhi
print()
print(df[(df["Age"]<25) | (df["Score"]>90)])  # Filter rows where Age is less than 25 or Score is greater than 90
print()

data = {'Name': ['Alice','Bob','Charlie','Diana','Ethan'],
        'City': ['Delhi','Mumbai','Pune','Delhi','Kolkata'],
        'Score':[88, 92, 75, 95, 80]}
df = pd.DataFrame(data)

print(df[df['City'].isin(['Delhi','Mumbai'])])  # Filter rows where City is either Delhi or Mumbai
print(df[(df['City']=="Mumbai") | (df['City']=="Delhi")])  # Filter rows where City is either Mumbai or Delhi
print()
print(df[df['Name'].str.contains('li')])  #Filter rows where Name contains the substring 'li'
print()

