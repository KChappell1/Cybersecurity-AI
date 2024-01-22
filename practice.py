import pandas as pd
from sklearn.model_selection import train_test_split


import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Practice_Dataset_iris.data.csv')

x = dataset.drop(columns=["Species"]).values
y = dataset["Species"].values
# print(y)

#Standardizes the x values
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y)

print(x_train)