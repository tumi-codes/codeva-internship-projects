import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


pd_sentiment = pd.read_csv("Data Set For Task/4) house Prediction Data Set.csv", sep=r"\s+",header=None)
pd_sentiment.columns = ['CRIM','ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(pd_sentiment.head())

#lineplots