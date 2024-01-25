import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Phishing_Legitimate_full.csv')

x = dataset.drop(columns=["id", "CLASS_LABEL"]).values
y = dataset["CLASS_LABEL"].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.80)

model = linear_model.LogisticRegression().fit(x_train, y_train)

print("Accuracy:", model.score(x_test, y_test))

print("*************")
print(dataset.shape)
print("*************")