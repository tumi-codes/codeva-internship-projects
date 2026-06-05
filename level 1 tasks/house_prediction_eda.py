import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd_sentiment = pd.read_csv("Data Set For Task/4) house Prediction Data Set.csv", sep=r"\s+",header=None)
pd_sentiment.columns = ['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(pd_sentiment.head())

# cleaning the dataset
pd_sentiment.dropna(inplace=True)  
pd_sentiment.drop_duplicates(inplace=True)  

# calculating the summary statistics
print(pd_sentiment[['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']].agg(['mean', 'median', 'std']))
print(pd_sentiment[['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']].mode())

# visualizations 
#histograms 
fig, ax = plt.subplots(2, 2, figsize = (12, 10))
# distribution of house prices(MEDV)
sns.histplot(data=pd_sentiment, x='MEDV', ax=ax[0, 0])
# distribution of number of rooms(RM)
sns.histplot(data=pd_sentiment, x='RM', ax=ax[0, 1])
# distribution of crime rate (CRIM)
sns.histplot(data=pd_sentiment, x='CRIM', ax=ax[1, 0])

plt.tight_layout()
plt.show()

#scatterplots
fig, ax = plt.subplots(2, 2, figsize= (12, 10))
# Number of rooms(RM) vs House price(MEDV)
sns.scatterplot(data=pd_sentiment, x='MEDV', y='RM', ax=ax[0, 0])
# Number of crime rate(CRIM) vs house price(MEDV)
sns.scatterplot(data=pd_sentiment, x='MEDV', y='CRIM', ax=ax[0, 1])
#lower status population vs house price
sns.scatterplot(data=pd_sentiment, x='MEDV', y='LSTAT', ax=ax[1, 0])

plt.tight_layout()
plt.show()

#boxplots
fig, ax = plt.subplots(1, 2, figsize= (12, 10))
#crime rate outliers(CRIM)
sns.boxplot(data=pd_sentiment, x='CRIM', ax=ax[0])
#house prices outliers (MEDV)
sns.boxplot(data=pd_sentiment, x='MEDV', ax=ax[1])

#finding correlations between prices(MEDV) and number of rooms (RM)
corr_matrix = pd_sentiment[['MEDV', 'RM']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
