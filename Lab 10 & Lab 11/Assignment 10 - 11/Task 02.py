#Task 02
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
df = pd.read_csv("/content/boston.csv")
print("Dataset Preview:")
print(df.head())
df.fillna(df.mean(numeric_only=True), inplace=True)
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
df = pd.get_dummies(df, drop_first=True)
target = "MEDV"
X = df.drop(target, axis=1)
y = df[target]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
lr_mae = mean_absolute_error(y_test, y_pred_lr)
lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
dt_mae = mean_absolute_error(y_test, y_pred_dt)
dt_rmse = np.sqrt(mean_squared_error(y_test, y_pred_dt))
print("\n========== MODEL PERFORMANCE ==========")
print("\nLinear Regression:")
print("MAE:", lr_mae)
print("RMSE:", lr_rmse)
print("\nDecision Tree:")
print("MAE:", dt_mae)
print("RMSE:", dt_rmse)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(y_test, y_pred_lr)
plt.title("Linear Regression")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.subplot(1,2,2)
plt.scatter(y_test, y_pred_dt)
plt.title("Decision Tree")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.tight_layout()
plt.show()
print("\n========== BEST MODEL ==========")
if dt_rmse < lr_rmse:
    print("Decision Tree is better (lower RMSE).")
else:
    print("Linear Regression is better (lower RMSE).")
