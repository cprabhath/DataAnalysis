import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


class Prediction:
    # Singleton class
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Prediction, cls).__new__(cls)
        return cls._instance

    # Constructor
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
        # read the csv file
        self.df = pd.read_csv('supermarket_sales.csv')

        # convert date column to date, month and week
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Week'] = self.df['Date'].dt.isocalendar().week

        # monthly sales analysis for each branch
        self.monthly_sales = self.df.groupby(['Month', 'Branch'])['Total'].sum().unstack()

        # convert the index to numpy array
        self.x = np.array(self.monthly_sales.index).reshape(-1, 1)
        self.y = self.monthly_sales.mean(axis=1).values

        self.model = LinearRegression()
        self.model.fit(self.x, self.y)

        self.next_months = np.array([max(self.x) + 1, max(self.x) + 2, max(self.x) + 3]).reshape(-1, 1)
        self.next_months_prediction = self.model.predict(self.next_months)

        # create a dataframe for the prediction
        self.prediction_df = pd.DataFrame({'Month': [13, 14, 15], 'Prediction Sales': self.next_months_prediction})

    def sales_prediction(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        plt.figure(figsize=(10, 6))
        plt.bar(self.x.flatten(), self.y, label="Actual Sales", color='blue', alpha=0.7)
        plt.bar(self.next_months.flatten(), self.next_months_prediction, label="Predicted Sales", color='orange',
                alpha=0.7)
        plt.title("Monthly Sales Analysis of Each Branch")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.legend()
        plt.show()
