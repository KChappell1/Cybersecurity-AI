import pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#accesses the data, sets the species to numerical values, and creates x and y variables
#Irirs-setosa = 0
#Iris-virginica = 1
#iris-versicolor = 2
data = pd.read_csv("Practice_Dataset_iris.data.csv")
data['Species'].replace(['Iris-setosa','Iris-virginica', 'Iris-versicolor'],[0,1,2],inplace=True)
x = data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]].values
y = data["Species"].values

#Standardizes the x values
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

#Splits the data into a training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y)

#Creates the logisitic regression model
model = linear_model.LogisticRegression().fit(x_train, y_train)

#Prints the accuracy and predictions of the model
print("Accuracy:", model.score(x_test, y_test))

print("*************")
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 4)
    y_pred = int(model.predict(x))

    if y_pred == 0:
        y_pred = "Iris-setosa"
    elif y_pred == 1:
        y_pred = "Iris-virginica"
    else:
        y_pred = "Iris-versicolor"
    
    actual = y_test[index]
    if actual == 0:
        actual = "Iris-setosa"
    elif actual == 1:
        actual = "Iris-virginica"
    else:
        actual = "Iris-versicolor"
    print("Predicted Species: " + y_pred + " Actual Species: " + actual)
    print("")