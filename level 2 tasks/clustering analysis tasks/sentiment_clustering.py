import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv('Data Set For Task/3) Sentiment dataset.csv')

# select numeric features for clustering
features = ['Likes', 'Retweets']
X = data[features]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# elbow method to find optimal k
inertias = []
k_range = range(1, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

# plot
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal k')
plt.xticks(k_range)
plt.grid(True)
plt.show()

# fit K-Means with chosen k (adjust based on elbow plot)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
data['cluster'] = kmeans.fit_predict(X_scaled)

# visualize clusters (2D scatter)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Likes', y='Retweets', hue='cluster', palette='viridis', s=60)
plt.title(f'K-Means Clustering (k={optimal_k}) on Sentiment Data')
plt.xlabel('Likes') 
plt.ylabel('Retweets')
plt.legend(title='Cluster')
plt.show()