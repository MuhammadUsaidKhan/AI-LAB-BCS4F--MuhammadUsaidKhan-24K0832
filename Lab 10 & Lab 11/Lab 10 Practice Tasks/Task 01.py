#LAB 10 Task 01
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv("/content/House_price.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)
df = pd.get_dummies(df, drop_first=True)
target = "Price"
X = df.drop(target, axis=1)
y = df[target]
print("\nTop Correlations with Price:")
print(df.corr()[target].sort_values(ascending=False))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n--- Model Performance ---")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
sample = X_test.iloc[0:1]
prediction = model.predict(sample)
print("\nPredicted Price:", prediction[0])
