import pandas as pd
from sklearn.model_selection import train_test_split
iris = pd.read_csv("/Users/sid404/Siddharth/College/OPEN SOURCE/Week 8/Iris.csv")
iris = iris.drop('Id',axis=1)
X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
print("\n80% train data:")
print(X_train)
print(y_train)
print("\n20% test data:")
print(X_test)
print(y_test)