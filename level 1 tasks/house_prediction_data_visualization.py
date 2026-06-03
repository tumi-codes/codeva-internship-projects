import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


pd_sentiment = pd.read_csv("Data Set For Task/4) house Prediction Data Set.csv", sep=r"\s+",header=None)
pd_sentiment.columns = ['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(pd_sentiment.head())

#histograms
fig, ax= plt.subplot(2, 2, figsize=(12, 10))
#Number of rooms vs house price
sns.histplot(data=pd_sentiment, x='RM', hue='MEDV', ax=ax[0, 0])
#Crime rate vs house price
sns.histplot(data=pd_sentiment, x='CRIM', hue='MEDV', ax=[0, 1])
#lower status population vs house price
sns.histplot(data=pd_sentiment, x='LSAT', hue='MEDV', ax=ax[1, 0])


#