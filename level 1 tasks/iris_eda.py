import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd_iris = pd.read_csv("Data Set For Task/1) iris.csv")

# cleaning the dataset
pd_iris.dropna(inplace=True)  
pd_iris.drop_duplicates(inplace=True)  

# calculating the summary statistics
print(pd_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].agg(['mean', 'median', 'std']))
print(pd_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mode())

# visualizations 
#histograms 
fig, ax = plt.subplots(2, 2, figsize = (12, 10))
sns.histplot(data=pd_iris, x='sepal_length', hue='species', ax=ax[0, 0])
sns.histplot(data=pd_iris, x='sepal_width', hue='species', ax=ax[0, 1])
sns.histplot(data=pd_iris, x='petal_length', hue='species', ax=ax[1, 0])
sns.histplot(data=pd_iris, x='petal_width', hue='species', ax=ax[1, 1])

plt.tight_layout()
plt.show()

#boxplots 
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
sns.boxplot(x='species', y='sepal_length', data=pd_iris, ax=ax[0, 0])
sns.boxplot(x='species', y='sepal_width', data=pd_iris, ax=ax[0, 1])
sns.boxplot(x='species', y='petal_length', data=pd_iris, ax=ax[1, 0])
sns.boxplot(x='species', y='petal_width', data=pd_iris, ax=ax[1, 1])

plt.tight_layout()
plt.show()

#scatter plots 
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=pd_iris, ax=ax[0, 0])
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=pd_iris, ax=ax[0, 1])
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=pd_iris, ax=ax[1, 0])
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=pd_iris, ax=ax[1, 1])

plt.tight_layout()
plt.show()

#finding correlations between numerical features
corr_matrix = pd_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()