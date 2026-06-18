import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv('Data Set For Task/2) Stock Prices Data Set.csv')
df['date'] = pd.to_datetime(df['date'])

# Select numeric features for clustering
features = ['open', 'high', 'low', 'close', 'volume']
X = df[features]

# Standardize 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method to find optimal k
inertias = []
k_range = range(1, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal k')
plt.xticks(k_range)
plt.grid(True)
plt.show()

# Fit K-Means with chosen k (adjust based on elbow plot)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualize clusters (2D scatter)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='close',
    y='volume',
    hue='cluster',
    palette='viridis',
    s=60
)
plt.title(f'K-Means Clustering (k={optimal_k}) on Stock Data')
plt.xlabel('Close Price')
plt.ylabel('Volume')
plt.show()

# Optional: see which symbols dominate each cluster
print(df.groupby('cluster')['symbol'].value_counts().groupby(level=0).head(5))