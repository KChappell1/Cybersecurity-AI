# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset
# Assuming you have a CSV file containing features extracted from executable files
dataset_path = 'malware_dataset.csv'
data = pd.read_csv(dataset_path)

# Step 3: Split data into features (X) and labels (y)
X = data.drop('label', axis=1)  # Assuming 'label' is the column indicating malware or not
y = data['label']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
predictions = model.predict(X_test)

# Step 7: Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Display detailed classification report
print("Classification Report:\n", classification_report(y_test, predictions))