import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd_iris = pd.read_csv('../Data Set For Task/iris.csv')

# cleaning the dataset
pd_iris.dropna(inplace=True)  
pd_iris.drop_duplicates(inplace=True)

# visualizations

# barplots of mean sepal length and width by species
sns.barplot(x='species', y='sepal_length', data=pd_iris)
sns.barplot(x='species', y='sepal_width', data=pd_iris)

#barplots of mean petal length and width by species
sns.barplot(x='species', y='petal_length', data=pd_iris)
sns.barplot(x='species', y='petal_width', data=pd_iris)

# line charts of sepal length and width by species
sns.lineplot(x='species', y='sepal_length', data=pd_iris)
sns.lineplot(x='species', y='sepal_width', data=pd_iris)

# line charts of petal length and width by species
sns.lineplot(x='species', y='petal_length', data=pd_iris)
sns.lineplot(x='species', y='petal_width', data=pd_iris)

#scatter plots of petal length and width by species
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=pd_iris)

# scatter plots of sepal length and width by species
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=pd_iris)

plt.show()