import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('Data Set For Task/3) Sentiment dataset.csv')

def predict_X_from_y(df, first, second):
    df_clean = df[[first, second]].dropna()  
    X = df_clean[[first]]
    y = df_clean[second]
    return train_test_split(X, y, test_size=0.2, random_state=42)

#model fitting and evaluation
def fit_model(df, first, second):
    X_train, X_test, y_train, y_test = predict_X_from_y(df, first, second)

    reg = LinearRegression()
    reg.fit(X_train, y_train)

    print(f"Intercept (b0): {reg.intercept_:.4f}")
    print(f"Coefficient (b1): {reg.coef_[0]:.4f}")

    y_pred = reg.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"R-squared: {r2:.4f}")
    print(f"MSE: {mse:.4f}")

    return reg, X_test, y_test, y_pred

#plot
def plot(df, first, second):
    reg, X_test, y_test, y_pred = fit_model(df, first, second)

    plt.figure(figsize=(8, 5))
    plt.scatter(X_test, y_test, color="steelblue", label="Actual")
    plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted")
    plt.xlabel(first)
    plt.ylabel(second)
    plt.title(f"{second} vs {first}")
    plt.legend()
    plt.tight_layout()
    plt.show()

#plot 