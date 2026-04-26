#LAB 11 Task 03
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [3.5, 2.8, 3.9, 2.5, 3.2, 3.8, 2.2, 3.0, 3.7, 2.6],
    'study_hours': [15, 8, 20, 5, 12, 18, 4, 10, 17, 6],
    'attendance_rate': [90, 70, 95, 60, 85, 92, 55, 80, 88, 65]
}
df = pd.DataFrame(data)
X = df[['GPA', 'study_hours', 'attendance_rate']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss = []
for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(2,7), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters
print("\nFinal Dataset with Clusters:")
print(df[['student_id', 'Cluster']])
plt.scatter(df['study_hours'], df['GPA'], c=clusters)
plt.title("Student Clusters (K-Means)")
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.show()
