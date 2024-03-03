from DataAnalysis import DataAnalysis
from Prediction import Prediction

data_analysis_instance = DataAnalysis()
prediction_instance = Prediction()

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

    # =============================User Input==================================
    user_input = int(input("Enter your choice: "))
    # ===========================End of User Input=============================

    # ===========================Exit from the application=====================
    if user_input == 8:
        print("==============Thank you for using our system==============")
        break
    # =============================End of Exit==================================
    else:
        # ==========Navigate to data analysis based on user input===============
        try:
            if user_input == 1:
                data_analysis_instance.monthly_sales()

            elif user_input == 2:
                data_analysis_instance.price_analysis()

            elif user_input == 3:
                data_analysis_instance.weekly_sales()

            elif user_input == 4:
                data_analysis_instance.distribution_of_sales()

            elif user_input == 5:
                data_analysis_instance.product_preference()

            elif user_input == 6:
                data_analysis_instance.payment_distribution()

            elif user_input == 7:
                prediction_instance.sales_prediction()

        # ========== End of Navigate to data analysis based on user input==========

        # =============================Invalid Input===============================
        except ValueError:
            print("Invalid Input. Please try Again!")
        # ===========================End of Invalid Input==========================
