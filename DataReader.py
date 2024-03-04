# panda used for data cleaning and graphical representation
import pandas as pd


# this class only responsible for reading the data from the csv file
class DataReader:
    def __init__(self):
        self.df = None

    def get_dataframe(self):
        self.df = pd.read_csv('supermarket_sales.csv')
        return self.df
