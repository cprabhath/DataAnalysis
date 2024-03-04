# panda used for data cleaning and graphical representation
import matplotlib.pyplot as plt
import pandas as pd

from DataReader import DataReader


class SalesAnalysis:

    def __init__(self):
        # read the data from the csv file
        self.df = DataReader().get_dataframe()
        # convert date column to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        # extract month
        self.df['Month'] = self.df['Date'].dt.month

    # monthly sales analysis for each branch
    def monthly_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        monthly_sales = self.df.groupby(['Month', 'Branch'])['Total'].sum().unstack()
        monthly_sales.plot(kind="bar", stacked=True, figsize=(10, 6))
        plt.title("Monthly Sales Analysis of Each Branch")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.show()
