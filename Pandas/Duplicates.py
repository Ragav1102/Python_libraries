import numpy as np
import pandas as pd

data = {'Name':  ['Alice','Bob','Alice','Charlie','Bob'],
        'Score': [88, 92, 88, 75, 92]}
df = pd.DataFrame(data)
print(df)
print()
print(df.duplicated())  #Check for duplicate rows
print()
print(df.drop_duplicates())  #Drop duplicate rows
print()

  
