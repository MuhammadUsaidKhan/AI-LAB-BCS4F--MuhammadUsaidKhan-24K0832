#LAB 10 Task 03
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv("/content/Shopping_data.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)
numeric_cols = df.select_dtypes(include=np.number).columns
df = df[(df[numeric_cols] < df[numeric_cols].quantile(0.99)).all(axis=1)]
target = "value"  # 1 = high-value, 0 = low-value
if target not in df.columns:
    print(f"Warning: Target column '{target}' not found after outlier removal. Please check the dataset structure.")
    target = "Spending Score (1-100)"
    print(f"Using '{target}' as the target column.")
X = df.drop(target, axis=1)
y = df[target]
scaler = StandardScaler() # Initialize the StandardScaler
X_numeric_cols = X.select_dtypes(include=np.number).columns
X_scaled_part = scaler.fit_transform(X[X_numeric_cols])
X_scaled_df = pd.DataFrame(X_scaled_part, columns=X_numeric_cols, index=X.index)
X = df.drop(target, axis=1)
non_numeric_X_cols = X.select_dtypes(exclude=np.number).columns
if len(non_numeric_X_cols) > 0:
    X = X.drop(columns=non_numeric_X_cols)
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2
)
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print("\n--- SVM Results (Hyperplane) ---")
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print("\n--- Decision Tree Results (Rules) ---")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))
