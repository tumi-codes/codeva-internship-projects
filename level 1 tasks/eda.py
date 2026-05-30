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
iris_mean = np.mean(pd_iris)
iris_median = np.median(pd_iris)
iris_mode = stats.mode(pd_iris)
iris_std = np.std(pd_iris)

# visualizations 
#histogram of sepal length
plt.hist(pd_iris['sepal_length'], bins=20, color='blue', alpha=0.7)
#boxplot of sepal width
sns.boxplot(data=pd_iris, y='sepal_width')
#scatter plot
pd_iris.plot(x='petal_length', y='petal_width', kind='scatter')
plt.show()

#finding correlations between numerical features
print(pd_iris['sepal_width'].corr(pd_iris['sepal_length']))
print(pd_iris['petal_length'].corr(pd_iris['petal_width']))