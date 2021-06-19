import pandas as pd
print("Shape of the data:")
data = pd.read_csv("/Users/sid404/Siddharth/College/OPEN SOURCE/Week 8/Iris.csv")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 3 rows:")
print(data.head(3))
