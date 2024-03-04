import matplotlib.pyplot as plt
import pandas as pd

from AnalysisComponent import AnalysisComponent
from DataReader import DataReader


class ProductPreference(AnalysisComponent):
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
        self.product_preference()

    # product preference analysis
    def product_preference(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        df_product_preference = self.df["Product line"].value_counts()
        df_product_preference.plot(kind="bar", figsize=(10, 6))
        plt.title("Product Preference Analysis")
        plt.xlabel("Product Line")
        plt.ylabel("Number of Sales")
        plt.show()
