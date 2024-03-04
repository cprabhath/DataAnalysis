from DataReader import DataReader
from DistributionOfSales import DistributionOfSales
from MonthlySalesAnalysis import MonthlySalesAnalysis
from AnalysisComponent import AnalysisComponent
from PriceAnalysis import PriceAnalysis
from ProductPreference import ProductPreference
from WeeklySales import WeeklySales


class DataAnalysis:
    # =============== Constructor ================
    def __init__(self):
        self.components = []
        self.data_reader = DataReader()
    # =============End of Constructor=============

    # =============Add component to the data analysis==============
    def add_component(self, component: AnalysisComponent):
        self.components.append(component)
    # =============End of adding component=========================


# ====== add all the components to the data analysis ==============
data_analysis = DataAnalysis()
data_analysis.add_component(MonthlySalesAnalysis())
data_analysis.add_component(PriceAnalysis())
data_analysis.add_component(WeeklySales())
data_analysis.add_component(DistributionOfSales())
data_analysis.add_component(ProductPreference())
# =================End of adding components========================
