import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd_iris = pd.read_csv('../Data Set For Task/iris.csv')

# cleaning the dataset
pd_iris.dropna(inplace=True)  
pd_iris.drop_duplicates(inplace=True)

pd_iris.plot(x='petal_length', y='petal_width', kind='bar', title='petal length vs width')
pd_iris.plot(x='sepal_length', y='sepal_width', kind='scatter', title='sepal width vs length')
pd_iris.plot(x='sepal_length', y='sepal_width', kind='line', title='scatter of sepal_width vs length')