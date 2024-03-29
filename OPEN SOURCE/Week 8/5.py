import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
boston = load_boston()
print(boston)
df_x = pd.DataFrame(boston.data, columns = boston.feature_names)
df_y = pd.DataFrame(boston.target)
df_x.describe()
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=42)
reg.fit(x_train, y_train)
print(reg.coef_)
y_pred = reg.predict(x_test)
print(y_pred)
y_pred[2]
y_test[0]
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))
