#Task 03
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("/content/marketing_campaign.csv", sep='\t')
print("Dataset Preview:")
print(df.head())
df.fillna(df.mean(numeric_only=True), inplace=True)
features = [
    'Income',
    'Recency',
    'MntWines',
    'MntFruits',
    'MntMeatProducts',
    'MntFishProducts',
    'MntSweetProducts'
]
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(2,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters
plt.scatter(df['Income'], df['MntWines'], c=clusters)
plt.title("Customer Segmentation")
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.show()
print("\nCustomer Clusters:")
print(df[['ID', 'Cluster']].head(20))
