batch1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Score': [88, 92]
})
 
batch2 = pd.DataFrame({
    'Name': ['Charlie', 'Diana'],
    'Score': [75, 95]
})

combined = pd.concat([batch1, batch2])
print(combined)

