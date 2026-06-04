import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd_sentiment = pd.read_csv("Data Set For Task/3) Sentiment dataset.csv")

# cleaning the dataset
pd_sentiment.dropna(inplace=True)  
pd_sentiment.drop_duplicates(inplace=True)  

# calculating the summary statistics
print(pd_sentiment[['Likes', 'Retweets']].agg(['mean', 'median', 'std']))
print(pd_sentiment[['Likes', 'Retweets']].mode())

#BOXPLOTS
fig, ax = plt.subplots(1, 2, figsize=(12, 10))
#Likes by sentiment
sns.boxplot(data=pd_sentiment, x='Likes', ax=ax[0])
#retweets by sentiments
sns.boxplot(data=pd_sentiment, x='Retweets', ax=ax[1])
plt.tight_layout()
plt.show()

#barplots
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
#sentiment count
sns.barplot(data=pd_sentiment, x='Sentiment', ax=ax[0, 0])
#posts per platform
sns.barplot(data=pd_sentiment, x='Platform', ax=ax[0,1])
#posts per country
sns.barplot(data=pd_sentiment, x='Country', ax=ax[1, 0])
#average likes per sentiment
sns.barplot(data=pd_sentiment, x='Sentiment', y='Likes', ax=ax[1, 1])

plt.tight_layout()
plt.show()

#correlation analysis
corr = pd_sentiment[['Likes','Retweets','Hour']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Correlation Matrix')
plt.show()