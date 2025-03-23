import pandas as pd
data={
    "Name": ["john","Alice","Bob","emma"],
    "duration": [25,23,24,22],
    "Gender":["Male","Female","Male","Female"],
    "Marks":[85,90,75,95]
    }
df=pd.DataFrame(data)
print(df)
print(df.loc[2])
print(df.shape)
for col in df:
    print(col)
