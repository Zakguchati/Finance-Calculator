import math

# Display the menu options for the user
menu = """ 
Investment - To calculate the total value of your investment after interest.
Bond - To calculate the monthly repayment amount on your home loan.
"""
print(menu)

# Get the user's decision on whether to calculate investment or bond repayment
decision = input("Enter either Investment or Bond to continue: ").lower()

# If the user decides to calculate investment...
if decision == 'investment':
    # Get the amount of money being deposited from the user
    property_value = float(input("Please enter the amount of money you're depositing: "))
    # Get the interest rate from the user and convert it to a decimal
    interest_rate = float(input("Please enter the interest rate (excluding %): ")) / 100
    # Get the number of years the user would like to invest
    time = int(input("Please enter the amount of years you would like to invest: "))
    
    # Get the user's choice of interest type (simple or compound)
    interest = input("Please choose between 'Simple' or 'Compound' interest: ").lower()
    
    # If the user chooses simple interest...
    if interest == "simple":
        # Calculate the total amount of interest the user will earn
        total_interest = property_value * (1 + interest_rate * time)
        # Round the result to two decimal places
        total_interest = round(total_interest, 2)
        # Display the result to the user
        print(f"The total amount of interest you'll earn on your investment is {total_interest}.")

    # If the user chooses compound interest...
    elif interest == "compound":
        # Calculate the total amount of interest the user will earn
        total_interest = property_value * math.pow((1 + interest_rate), time)
        # Round the result to two decimal places
        total_interest = round(total_interest, 2)
        # Display the result to the user
        print(f"The total amount of interest you'll earn on your investment is {total_interest}.")
    
    # If the user enters an invalid interest type...
    else:
        # Display an error message
        print("Invalid input. Please choose 'Simple' or 'Compound'.")

# If the user decides to calculate bond repayment...
elif decision == 'bond':
    # Get the present value of the house from the user
    property_value = float(input("Please enter the present value of the house: "))
    # Get the monthly interest rate from the user and convert it to a decimal
    interest_rate = float(input("Please enter the monthly interest rate (as a percentage): ")) / 100 / 12
    # Get the number of months the user plans to repay the bond
    months = int(input("Please enter the amount of months you plan to take to repay the bond: "))
    
    # Calculate the monthly repayment amount
    repayment = (interest_rate * property_value) / (1 - math.pow((1 + interest_rate), -months))
    # Round the monthly repayment amount to two decimal places
    repayment = round(repayment, 2)
    
    # Display the monthly repayment amount to the user
    print(f"The amount of money you'll have to pay each month is £{repayment}.")

# If the user enters an invalid decision...
else:
    # Display an error message
    print("Invalid input. Please enter 'Investment' or 'Bond'.")






        



