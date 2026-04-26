#LAB 11 Task 01
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
df = pd.read_csv("/content/Mall_Customers.csv")
X = df.drop("CustomerID", axis=1)
X = pd.get_dummies(X, drop_first=True)
print("\n========== WITHOUT SCALING ==========")
kmeans1 = KMeans(n_clusters=5, random_state=42)
labels1 = kmeans1.fit_predict(X)
print("WCSS:", kmeans1.inertia_)
print("Silhouette Score:", silhouette_score(X, labels1))
print("\n========== WITH SCALING ==========")
age = X[['Age']]
other_features = X.drop("Age", axis=1)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(other_features)
X_scaled = np.concatenate([age.values, scaled_features], axis=1)
kmeans2 = KMeans(n_clusters=5, random_state=42)
labels2 = kmeans2.fit_predict(X_scaled)
print("WCSS:", kmeans2.inertia_)
print("Silhouette Score:", silhouette_score(X_scaled, labels2))
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=labels1)
plt.title("Without Scaling")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.subplot(1,2,2)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=labels2)
plt.title("With Scaling")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()
