import matplotlib.pyplot as plt
import pandas as pd

from AnalysisComponent import AnalysisComponent
from DataReader import DataReader


class WeeklySales(AnalysisComponent):
    def __init__(self):
        # Initialize and read the data from the CSV file
        self.df = DataReader().get_dataframe()
        self.prepare_data()

    def prepare_data(self):
        # Convert date column to datetime and extract month
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Week'] = self.df['Date'].dt.isocalendar().week

    def perform_analysis(self, data=None):
        if data is not None:
            self.df = data
            self.prepare_data()
        self.weekly_sales()

    def weekly_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        df_weekly_sales = self.df.groupby(["Week"])["Total"].sum()
        df_weekly_sales.plot(kind="line", marker="o", figsize=(10, 6))
        plt.title("Weekly Sales Analysis of Supermarket Network")
        plt.xlabel("Week")
        plt.ylabel("Total Sales")
        plt.show()
