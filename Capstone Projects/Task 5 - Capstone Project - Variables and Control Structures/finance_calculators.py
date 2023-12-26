# This Python program is designed for the user to access financial calculators: investment and home loan calculator depending on their choice
import math

# Get input from user on the choice of calculator they would require depending on the options given
print("investment - to calculate the amount of interest you'll earn on your investment\n\
bond       - to calculate the amount you'll have to pay on a home loan")

opt_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

opt_calculator = opt_calculator.lower()

""" Using control structures: if, elif, else statments, 
required values got from user and formula used accordingly for investment (simple / compound interest) and bond calculator

Formula used for investment calculator:
1) Simple interest: A = P(1 + r * t)
2) Compound interest: A = P(1 + r) ^ t
where A - total amount after applying interest
      P - Amount the user deposits
      r - interest rate
      t - number of years the amount is deposited
Formula used for bond calculator:
repayment = (i * P) / ((1 - (1 + i)) ^ (-n))
where i - monthly interest rate i.e. 7% monthly interest rate = (7/100)/12
      n - number of months by which bond will be repaid
"""
if opt_calculator == "investment":
    print("Please enter the following details for investment calculation")
    deposit_amount = int(input("Amount you would like to invest: "))
    expected_int_rate = float(input("Interest rate you are expecting: "))
    interest_rate = expected_int_rate/100
    no_of_years = int(input("Number of years you would invest: "))
    interest = input("Enter your choice of interest component (i.e.) simple or compound: ")
    interest = interest.lower()
    if interest == "simple":
        total_amount = deposit_amount * (1 + interest_rate * no_of_years)
        print (f"You will earn {total_amount}, if you deposit {deposit_amount} for {no_of_years} years with {expected_int_rate} % interest rate")
    elif interest == "compound":
        total_amount = round(deposit_amount * math.pow((1 + interest_rate) , no_of_years),2)
        print (f"You will earn {total_amount}, if you deposit {deposit_amount} for {no_of_years} years with {expected_int_rate} % interest rate")
elif opt_calculator == "bond": 
    print("Please enter the following details for home loan / bond calculation")
    value_of_house_present = int(input("Present value of house: "))
    interest_rate = float(input("Interest rate: "))
    calc_interest_rate = (interest_rate/100)/12
    no_of_months = int(input("Number of months the bond will be repaid: "))
    repayment = round((calc_interest_rate * value_of_house_present) / (1 - (1 + calc_interest_rate) ** (-no_of_months)),2)
    print(f"You will have to repay {repayment} every month")
else:
    print("Incorrect choice!")