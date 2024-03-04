from AnalysisComponent import AnalysisComponent
from DataReader import DataReader
import pandas as pd
import matplotlib.pyplot as plt


class MonthlySalesAnalysis(AnalysisComponent):
    def __init__(self):
        # Initialize and read the data from the CSV file
        self.df = DataReader().get_dataframe()
        self.prepare_data()

    def prepare_data(self):
        # Convert date column to datetime and extract month
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month'] = self.df['Date'].dt.month

    def perform_analysis(self, data=None):
        if data is not None:
            self.df = data
            self.prepare_data()
        self.monthly_sales()

    def monthly_sales(self):
        print("Please wait, analyzing your dataset... This may take a few minutes.")
        monthly_sales = self.df.groupby(['Month', 'Branch'])['Total'].sum().unstack()
        monthly_sales.plot(kind="bar", stacked=True, figsize=(10, 6))
        plt.title("Monthly Sales Analysis of Each Branch")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.show()
