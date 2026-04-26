#LAB 11 Task 02
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}
df = pd.DataFrame(data)
print("Dataset:\n", df)
X = df.drop("vehicle_serial_no", axis=1)
X = pd.get_dummies(X, columns=['vehicle_type'], drop_first=True)
print("\n========== WITHOUT SCALING ==========")
kmeans1 = KMeans(n_clusters=3, random_state=42)
labels1 = kmeans1.fit_predict(X)
df["Cluster_No_Scaling"] = labels1
print("Clusters:\n", df[["vehicle_serial_no", "Cluster_No_Scaling"]])
print("WCSS:", kmeans1.inertia_)
print("Silhouette Score:", silhouette_score(X, labels1))
print("\n========== WITH SCALING ==========")
num_cols = ['mileage', 'fuel_efficiency', 'maintenance_cost']
cat_cols = [col for col in X.columns if col not in num_cols]
scaler = StandardScaler()
X_scaled_num = scaler.fit_transform(X[num_cols])
X_scaled = np.concatenate([X_scaled_num, X[cat_cols].values], axis=1)
kmeans2 = KMeans(n_clusters=3, random_state=42)
labels2 = kmeans2.fit_predict(X_scaled)
df["Cluster_With_Scaling"] = labels2
print("Clusters:\n", df[["vehicle_serial_no", "Cluster_With_Scaling"]])
print("WCSS:", kmeans2.inertia_)
print("Silhouette Score:", silhouette_score(X_scaled, labels2))
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(df['mileage'], df['maintenance_cost'], c=labels1)
plt.title("Without Scaling")
plt.xlabel("Mileage")
plt.ylabel("Maintenance Cost")
plt.subplot(1,2,2)
plt.scatter(df['mileage'], df['maintenance_cost'], c=labels2)
plt.title("With Scaling")
plt.xlabel("Mileage")
plt.ylabel("Maintenance Cost")
plt.show()
