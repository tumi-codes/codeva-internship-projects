import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd_stock_prices = pd.read_csv('Data Set For Task/2) Stock Prices Data Set.csv')

# cleaning the dataset
pd_stock_prices.dropna(inplace=True)  
pd_stock_prices.drop_duplicates(inplace=True)  

#Distribution of Closing Prices
sns.histplot(pd_stock_prices['close'], kde=True)
plt.title('Distribution of Closing Prices')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.show()

#Volume Distribution
sns.histplot(pd_stock_prices['volume'], kde=True)
plt.title('Distribution of Trading Volume')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.show()

#closing price over time
plt.figure(figsize=(12, 6))
plt.plot(pd_stock_prices['date'], pd_stock_prices['close'])
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()

#trading volume over time
plt.figure(figsize=(12, 6))
plt.plot(pd_stock_prices['date'], pd_stock_prices['volume'])
plt.title('Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

#correlation analysis
correlation_matrix = pd_stock_prices[['open', 'high', 'low', 'close', 'volume']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

#outlier detection using boxplots
sns.boxplot(y=pd_stock_prices['close'])
plt.title('Close Price Outliers')
plt.show()