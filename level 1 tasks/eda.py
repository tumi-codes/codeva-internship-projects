import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


pd_iris = pd.read_csv("../Data Set For Task/1) iris.csv")

# cleaning the dataset
pd_iris.dropna(inplace=True)  
pd_iris.drop_duplicates(inplace=True)  

# calculate the summary statistics
pd_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].agg(['mean', 'median', 'mode'])
pd_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mode()

# visualizations 
#histograms of sepal length and width
sns.histplot(pd_iris['sepal_length'])
sns.histplot(pd_iris['sepal_width'])

#histograms of petal length and width
sns.histplot(pd_iris['petal_length'])
sns.histplot(pd_iris['petal_width'])

#boxplots of sepal length and width by species
sns.boxplot(x='species', y='sepal_length', data=pd_iris)
sns.boxplot(x='species', y='sepal_width', data=pd_iris)

#boxplots of petal length and width by species
sns.boxplot(x='species', y='petal_length', data=pd_iris)
sns.boxplot(x='species', y='petal_width', data=pd_iris)

#scatter plots of sepal length and width by species
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=pd_iris)
#scatter plots of petal length and width by species
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=pd_iris)

plt.show()

#finding correlations between numerical features
#correlation between sepal length and width
print(pd_iris['sepal_width'].corr(pd_iris['sepal_length']))
#correlation between petal length and width
print(pd_iris['petal_length'].corr(pd_iris['petal_width']))