#Task 01
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample
df = pd.read_csv("/content/creditcard.csv")
print("Dataset Shape:", df.shape)
print(df.head())
df_majority = df[df.Class == 0]
df_minority = df[df.Class == 1]
print("\nBefore Balancing:")
print(df['Class'].value_counts())
df_majority_downsampled = resample(
    df_majority,
    replace=False,
    n_samples=len(df_minority),
    random_state=42
)
df_balanced = pd.concat([df_majority_downsampled, df_minority])
print("\nAfter Balancing:")
print(df_balanced['Class'].value_counts())
X = df_balanced.drop("Class", axis=1)
y = df_balanced["Class"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
lr_acc = accuracy_score(y_test, y_pred_lr)
lr_prec = precision_score(y_test, y_pred_lr)
lr_rec = recall_score(y_test, y_pred_lr)
lr_f1 = f1_score(y_test, y_pred_lr)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
rf_acc = accuracy_score(y_test, y_pred_rf)
rf_prec = precision_score(y_test, y_pred_rf)
rf_rec = recall_score(y_test, y_pred_rf)
rf_f1 = f1_score(y_test, y_pred_rf)

print("\n========== MODEL COMPARISON ==========")
print("\nLogistic Regression:")
print("Accuracy:", lr_acc)
print("Precision:", lr_prec)
print("Recall:", lr_rec)
print("F1 Score:", lr_f1)
print("\nRandom Forest:")
print("Accuracy:", rf_acc)
print("Precision:", rf_prec)
print("Recall:", rf_rec)
print("F1 Score:", rf_f1)
print("\n========== BEST MODEL ==========")
if rf_f1 > lr_f1:
    print("Random Forest is better (higher F1-score).")
else:
    print("Logistic Regression is better (higher F1-score).")
