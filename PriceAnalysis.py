from AnalysisComponent import AnalysisComponent
from DataReader import DataReader
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class PriceAnalysis(AnalysisComponent):
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
        self.product_analysis()

    def product_analysis(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        plt.figure(figsize=(12, 12))
        sns.boxplot(x="Product line", y="Unit price", data=self.df)
        plt.title("Price Analysis of Each product")
        plt.xlabel("Product Line")
        plt.ylabel("Unit Price")
        plt.xticks(rotation=45, ha="right")
        plt.show()
