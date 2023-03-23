import numpy as np
import pandas as pd

# dataSet = pd.read_csv("automobile_data.csv")
# print(dataSet)
# print(dataSet.head())
# print(dataSet.tail())
# print(dataSet.columns)
# print((dataSet.nunique()))
# print(dataSet.isnull().sum())

# newData = dataSet.drop([0,1,2], axis=0)

# dataSet.dropna(subset=dataSet.columns, inplace=True)

# print(dataSet)
# print(dataSet)


#################### part b
df = pd.read_csv("automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})

# print (df[["company", "price"]][df.price == df["price"].max()])
# print(df[df.company == "toyota"])
print(df.groupby("company")["company", "price"].size())
