import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv('Data Set For Task/4) house Prediction Data Set.csv', sep=r"\s+",header=None)
data.columns = ['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# select numeric features for clustering
features = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = data[features]

# standardize
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

# fit k-means with chosen k
optimal_k = 3  # Adjust based on elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
data['cluster'] = kmeans.fit_predict(X_scaled)

# visualize using scatters
plt.figure(figsize=(12, 10))
sns.scatterplot(data=data, x='RM', y='MEDV', hue='cluster', palette='viridis', s=60)
plt.title(f'K-Means Clustering (k={optimal_k}) on House Data')  
plt.xlabel('Average number of rooms (RM)')
plt.ylabel('Median value of owner-occupied homes (MEDV)')
plt.legend(title='Cluster')
plt.show()