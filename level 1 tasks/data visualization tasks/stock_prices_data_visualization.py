import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd_stock_prices = pd.read_csv('Data Set For Task/2) Stock Prices Data Set.csv')

# cleaning the dataset
pd_stock_prices.dropna(inplace=True)  
pd_stock_prices.drop_duplicates(inplace=True)

#scatter plots to visualize relationships between variables
fig, ax = plt.subplots(2, 2, figsize=(12,10))

sns.scatterplot(x='open', y='close', data=pd_stock_prices, ax=ax[0,0])
ax[0,0].set_title('Open vs Close')

sns.scatterplot(x='high', y='low', data=pd_stock_prices, ax=ax[0,1])
ax[0,1].set_title('High vs Low')

sns.scatterplot(x='volume', y='close', data=pd_stock_prices, ax=ax[1,0])
ax[1,0].set_title('Volume vs Close')

sns.scatterplot(x='volume', y='open', data=pd_stock_prices, ax=ax[1,1])
ax[1,1].set_title('Volume vs Open')

plt.tight_layout()
plt.show()

#boxplots to visualize distribution and outliers
fig, ax = plt.subplots(2, 2, figsize=(12,10))

sns.boxplot(y='open', data=pd_stock_prices, ax=ax[0,0])
ax[0,0].set_title('Open')

sns.boxplot(y='high', data=pd_stock_prices, ax=ax[0,1])
ax[0,1].set_title('High')

sns.boxplot(y='low', data=pd_stock_prices, ax=ax[1,0])
ax[1,0].set_title('Low')

sns.boxplot(y='close', data=pd_stock_prices, ax=ax[1,1])
ax[1,1].set_title('Close')

plt.tight_layout()
plt.show()

#line plots to visualize trends over time
#closing price over time
plt.figure(figsize=(12,5))

sns.lineplot(x='date', y='close', data=pd_stock_prices)

plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')

plt.show()

#trading volume over time
plt.figure(figsize=(12,5))

sns.lineplot(x='date', y='volume', data=pd_stock_prices)

plt.title('Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

#open vs close trends
plt.figure(figsize=(12,5))

sns.lineplot(x='date', y='open', data=pd_stock_prices, label='Open')
sns.lineplot(x='date', y='close', data=pd_stock_prices, label='Close')

plt.title('Open and Close Prices Over Time')

plt.legend()

plt.show()