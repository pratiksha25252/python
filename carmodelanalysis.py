import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={
     'car': ['Sedan A', 'SUV B', 'Coupe C', 'Sedan A', 'SUV B', 'Coupe C', 'Sedan A'],
    'year':      [2018,      2019,     2020,     2021,      2022,     2023,     2024],
    'price':     [20000,     35000,    27000,    22000,     37000,    29000,    23000],
    'mileage':   [30000,     25000,    15000,    28000,     23000,    14000,    26000]
}

df=pd.DataFrame(data)
print(df['price'].mean())
avgprice=df.groupby('car')['price'].mean()
print(avgprice)
minmilege=df['mileage'].idxmin()
carmin=df.loc[minmilege,'car']
print(carmin)
plt.xlabel('Car Model')
plt.ylabel('Average Price')
plt.title('Average Price per Car Model')
plt.barh(avgprice.index,avgprice,color='blue')
plt.show()
plt.hist(df['mileage'],bins=20)
plt.show()
goodcars=(df[(df['price']<50000) & (df['mileage']<50000)])
print(goodcars)
plt.scatter(df['price'],df['mileage'],color='blue',label='good value cars',s=100)
plt.axhline(20000, color='red', linestyle='--', label='Price = $20,000')
plt.axvline(50000, color='blue', linestyle='--', label='Mileage = 50,000')
plt.grid(True)
plt.legend()



