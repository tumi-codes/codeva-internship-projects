import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd_iris = pd.read_csv('Data Set For Task/1) iris.csv')

# cleaning the dataset
pd_iris.dropna(inplace=True)  
pd_iris.drop_duplicates(inplace=True)

# visualizations

# barplots
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
sns.barplot(x='species', y='sepal_length', data=pd_iris, ax=ax[0,0], label='Sepal Length')
sns.barplot(x='species', y='sepal_width', data=pd_iris, ax=ax[0,1], label='Sepal Width')
sns.barplot(x='species', y='petal_length', data=pd_iris, ax=ax[1,0], label='Petal Length')
sns.barplot(x='species', y='petal_width', data=pd_iris, ax=ax[1,1], label='Petal Width')

ax[0, 1].set_title('Sepal Length')
ax[0, 1].set_title('Sepal Width')
ax[0, 1].set_title('Petal Length')
ax[0, 1].set_title('Petal Width')
plt.tight_layout()
plt.savefig('bar plots iris.pdf', dpi=300, bbox_inches='tight')
plt.show()

# line charts
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
sns.lineplot(x='species', y='sepal_length', data=pd_iris, ax=ax[0, 0], label='Sepal Length')
sns.lineplot(x='species', y='sepal_width', data=pd_iris, ax=ax[0, 1], label='Sepal Width')
sns.lineplot(x='species', y='petal_length', data=pd_iris, ax=ax[1, 0], label='Petal Length')
sns.lineplot(x='species', y='petal_width', data=pd_iris, ax=ax[1, 1], label='Petal Width')

ax[0, 1].set_title('Sepal Length')
ax[0, 1].set_title('Sepal Width')
ax[0, 1].set_title('Petal Length')
ax[0, 1].set_title('Petal Width')
plt.tight_layout()
plt.savefig('line charts iris.pdf', dpi=300, bbox_inches='tight')
plt.show()

#scatter plots
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=pd_iris, ax=ax[0, 0])
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=pd_iris, ax=ax[0, 1])
sns.scatterplot(x='sepal_length', y='petal_width', hue='species', data=pd_iris, ax=ax[1, 0])
sns.scatterplot(x='petal_length', y='sepal_width', hue='species', data=pd_iris, ax=ax[1, 1])

plt.tight_layout()
plt.savefig('scatter plots iris.pdf', dpi=300, bbox_inches='tight')
plt.show()