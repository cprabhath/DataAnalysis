# panda used for data cleaning and graphical representation
import pandas as pd
import matplotlib.pyplot as plt
# used for analysis representation
import seaborn as sns


class DataAnalysis:
    # Singleton class
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataAnalysis, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # check if the class is already initialized
        if not hasattr(self, 'initialized'):
            self.initialized = True

        # read the csv file
        self.df = pd.read_csv('supermarket_sales.csv')

        # convert date column to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        # extract month and Week from date
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Year'] = self.df['Date'].dt.year
        self.df['Week'] = self.df['Date'].dt.isocalendar().week

    # monthly sales analysis for each branch
    def monthly_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        monthly_sales = self.df.groupby(['Month', 'Branch'])['Total'].sum().unstack()
        monthly_sales.plot(kind="bar", stacked=True, figsize=(10, 6))
        plt.title("Monthly Sales Analysis of Each Branch")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.show()

    # monthly sales analysis for each branch per year
    def monthly_sales_per_year(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        monthly_sales = self.df.groupby(['Month', 'Year', 'Branch'])['Total'].sum().unstack()
        monthly_sales.plot(kind="bar", stacked=True, figsize=(10, 10))
        plt.title("Monthly Sales Analysis of Each Branch per Year")
        plt.xticks(ticks=range(0, 12),
                   labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'])
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.show()

    # Price analysis of each product using seaborn and matplotlib
    def price_analysis(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        plt.figure(figsize=(12, 12))
        sns.boxplot(x="Product line", y="Unit price", data=self.df)
        plt.title("Price Analysis of Each product")
        plt.xlabel("Product Line")
        plt.ylabel("Unit Price")
        plt.xticks(rotation=45, ha="right")
        plt.show()

    # Weekly sales analysis of the supermarket network
    def weekly_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        df_weekly_sales = self.df.groupby(["Week"])["Total"].sum()
        df_weekly_sales.plot(kind="line", marker="o", figsize=(10, 6))
        plt.title("Weekly Sales Analysis of Supermarket Network")
        plt.xlabel("Week")
        plt.ylabel("Total Sales")
        plt.show()

    # product preference analysis
    def product_preference(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        df_product_preference = self.df["Product line"].value_counts()
        df_product_preference.plot(kind="bar", figsize=(10, 6))
        plt.title("Product Preference Analysis")
        plt.xlabel("Product Line")
        plt.ylabel("Number of Sales")
        plt.show()

    # Analysis of distribution of total sales amount of purchases using seaborn and matplotlib
    def distribution_of_sales(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df["Total"], bins=20, kde=True)
        plt.title("Distribution of total sales Amount")
        plt.xlabel("Total Sales Amount")
        plt.ylabel("Frequency")
        plt.show()

    # Pie chart for payment type distribution
    def payment_distribution(self):
        print("Please wait, Analyzing your dataset... this may take few minutes")
        df_payment_method = self.df["Payment"].value_counts()
        df_payment_method.plot(kind="pie", figsize=(8, 6), autopct="%1.1f%%")
        plt.title("Payment Type Distribution")
        plt.show()
