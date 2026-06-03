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

#correlation analysis
corr = pd_sentiment[['Likes','Retweets','Hour']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Correlation Matrix')
plt.show()