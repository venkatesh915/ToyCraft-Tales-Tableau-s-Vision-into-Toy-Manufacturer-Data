# ----------------------------
# model.py
# ----------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# 1. Load dataset
data_file = "data.csv"   # Your main CSV
data = pd.read_csv(data_file)
print("Data Loaded Successfully")
print("Columns:", list(data.columns))

# 2. Define target
target_column = "Rating"

# 3. Prepare features (drop target)
X = data.drop(columns=[target_column])
y = data[target_column]

# 4. Encode categorical columns
categorical_cols = X.select_dtypes(include='object').columns
le_dict = {}
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    le_dict[col] = le  # Save encoder if needed later

# 5. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained successfully!")

# 7. Predict on entire dataset
y_pred = model.predict(X)

# 8. Save predictions alongside original data
predictions = data.copy()
predictions["Rating_predicted"] = y_pred

# Save CSV in UTF-8 for Tableau
predictions.to_csv("predictions_clean.csv", index=False, encoding='utf-8')
print("Predictions saved to predictions_clean.csv")
print("First 10 predictions:", y_pred[:10])