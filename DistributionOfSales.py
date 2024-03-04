from AnalysisComponent import AnalysisComponent
from DataReader import DataReader
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DistributionOfSales(AnalysisComponent):
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
        self.distribution_of_sales()

    def distribution_of_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df["Total"], bins=20, kde=True)
        plt.title("Distribution of total sales Amount")
        plt.xlabel("Total Sales Amount")
        plt.ylabel("Frequency")
        plt.show()
