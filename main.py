from DataAnalysis import data_analysis
from DistributionOfSalesCommand import DistributionOfSalesCommand
from MonthlySalesCommand import MonthlySalesCommand
from PriceAnalysisCommand import PriceAnalysisCommand
from ProductPreferenceCommand import ProductPreferenceCommand
from WeeklySalesCommand import WeeklySalesCommand

# ===================Command Pattern===================
commands = {
    1: MonthlySalesCommand(data_analysis.components[0]),
    2: PriceAnalysisCommand(data_analysis.components[1]),
    3: WeeklySalesCommand(data_analysis.components[2]),
    4: DistributionOfSalesCommand(data_analysis.components[3]),
    5: ProductPreferenceCommand(data_analysis.components[4]),
}
# =================End of Command Pattern================

while True:
    # =============================User Interface=============================
    print("=================Welcome to Sampath Food city=================")
    print("===================Data Analysis Department===================")
    print("1. Monthly sales analysis of each branch")
    print("2. Price analysis of Each product")
    print("3. Weekly sales analysis of supermarket network")
    print("4. Distribution of total sales amount of purchases")
    print("5. Product preference analysis")
    print("6. Distribution of payments types")
    print("7. Sales Prediction for next 3 months")
    print("8. Exit from the application")
    # ===========================End of User Interface=========================
    try:
        # =============================User Input==================================
        user_input = int(input("Enter your choice: "))
        # ===========================End of User Input=============================
        if user_input in commands:
            commands[user_input].execute()
        elif user_input == 8:
            print("==============Thank you for using our system==============")
            break
        else:
            print("Invalid choice, please try again.")

    # =============================Invalid Input===============================
    except ValueError:
        print("Invalid Input. Please try Again!")
        break
    # ===========================End of Invalid Input==========================


