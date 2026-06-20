import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd_sentiment = pd.read_csv('Data Set For Task/3) Sentiment dataset.csv')

#barplots
fig, ax = plt.subplots(1, 2, figsize=(12, 10))

#engagement per platform
sns.barplot(x='Platform', y='Likes', data=pd_sentiment, ax=ax[0])
sns.barplot(x='Platform', y='Retweets', data=pd_sentiment, ax=ax[1])

plt.tight_layout()
plt.show()

#scatterplots
fig, ax = plt.subplots(1, 2, figsize=(12, 10))
sns.scatterplot(data=pd_sentiment, x='Likes', y='Retweets', ax=ax[0])
sns.scatterplot(data=pd_sentiment, x='Hour', y='Likes', ax=ax[1])
plt.tight_layout()
plt.show()

#line charts
fig, ax = plt.subplots(1, 2, figsize=(12, 10))
sns.lineplot(data=pd_sentiment, x='Hour', y='Likes', ax=ax[0])
sns.lineplot(data=pd_sentiment, x='Hour', y='Retweets', ax=ax[1])
plt.tight_layout()
plt.show()