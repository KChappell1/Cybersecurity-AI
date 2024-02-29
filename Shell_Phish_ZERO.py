import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Phishing_Legitimate_full.csv')

x = dataset.drop(columns=["id", "CLASS_LABEL"]).values
y = dataset["CLASS_LABEL"].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10)

model = linear_model.LogisticRegression().fit(x_train, y_train)

print("Accuracy:", model.score(x_test, y_test))

print("*************")

for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 48)
    y_pred = int(model.predict(x))

    if y_pred == 0:
        y_pred = "Not Phishing"
    else:
        y_pred = "Phishing"
    
    actual = y_test[index]
    if actual == 0:
        actual = "Not Phishing"
    else:
        actual = "Phishing"
    print("Predicted Phishing: " + y_pred + " Actual: " + actual)


print("****TEST*****")
y_pred=int(model.predict([[2,1,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,1,0,0,0,0,0.0353982301,1.0000000000,1,0,0,0,0,0.0132743363,0,0,0,0,0,1,0,0,1,1,-1,1,0,1]]))

if y_pred == 0:
    y_pred = "Not Phishing"
else:
    y_pred = "Phishing"

print("Predicted:" , y_pred)
print("")