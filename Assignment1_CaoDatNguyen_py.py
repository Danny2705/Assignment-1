# Author: Cao Dat Nguyen
# Date: 2/2/2023
# This Program is a bill interaction between the customers and the calculator
# It will let them know how much the bill is based on the amount the customers use

# Greeting to customers about the Global Energy Bill calculator
print("Welcome to the Global Energy Bill calculator!")

# Ask customers to type their information about the bill.
account = input("Enter your account number: ")
month_number = input("Enter the month number(e.g., for January, enter 1): ")
electricity_plan = input("Enter your electricity plan (EFIR or EFLR): ").upper()

# Store the variables
tax_rate = 0
prices = 0
monthly_fee = 120.62
monthly_gas_transaction_fee = 1.32

# Check if the customers type electricity plan correct and ask them to type again if wrong
if electricity_plan != "EFIR" and electricity_plan != "EFLR":
    print("Please type the information again!")
    electricity_plan = input("Enter your electricity plan (EFIR or EFLR): ").upper()

# Ask customers to type their next information
electricity_used = input("Enter the electricity used in month " + month_number + " (in kWh): ")
electricity_used = float(electricity_used)
gas_plan = input("Enter your gas plan (GFIR or GFLR): ").upper()

# Check if the customers type the gas plan correct and ask them to type again if wrong
if gas_plan != "GFIR" and gas_plan != "GFLR":
    print("Please type the correct information again!")
    gas_plan = input("Enter your gas plan (GFIR or GFLR): ").upper()

# Ask customers to type their next information
gas_used = float(input("Enter the amount of gas you used in month " + month_number + " (in GJ): "))
province = input("Enter the abbreviation for your province of residence (two letters): ").upper()

# Check if the customers type the province correct and ask them to type again if wrong
if province != "AB" and province != "BC" and province != "MB" and province != "NT" and province != "NU" and \
        province != "QC" and province != "SK" and province != "YT" and province != "ON" and province != "NB" and \
        province != "NL" and province != "NS" and province != "PE":
    print("Please type the correct information again!")
    province = input("Enter the abbreviation for your province of residence (two letters): ").upper()

# Calculator will process with the province customers are living
if province == "NB" or province == "NL" or province == "NS" or province == "PE":
    tax_rate = 0.15
elif province == "ON":
    tax_rate = 0.13
else:
    tax_rate = 0.05

# Calculate the price of the electricity and gas plan with 4 cases:
if electricity_plan == "EFIR" and gas_plan == "GFIR":
    if electricity_used <= 1000 and gas_used <= 950:
        prices = 8.36 * electricity_used + 4.56 * gas_used
    elif electricity_used <= 1000 and gas_used > 950:
        prices = 8.36 * electricity_used + 4.56 * 950 + 5.89 * (gas_used - 950)
    elif electricity_used > 1000 and gas_used <= 950:
        prices = 1000 * 8.36 + 9.41 * (electricity_used - 1000) + 4.56 * gas_used
    else:
        prices = 1000 * 8.36 + 9.41 * (electricity_used - 1000) + 4.56 * 950 + 5.89 * (gas_used - 950)
elif electricity_plan == "EFIR" and gas_plan == "GFLR":
    if electricity_used <= 1000:
        prices = 8.36 * electricity_used + 3.93 * gas_used
    else:
        prices = 1000 * 8.36 + 9.41 * (electricity_used - 1000) + 3.93 * gas_used
elif electricity_plan == "EFLR" and gas_plan == "GFIR":
    if gas_used <= 950:
        prices = 9.11 * electricity_used + 4.56 * gas_used
    else:
        prices = 9.11 * electricity_used + 4.56 * 950 + 5.89 * (gas_used - 950)
else:
    prices = 9.11 * electricity_used + 3.93 * gas_used

# Give the total amount that the customers use
canadian_dollars = prices * 0.01
total = float(monthly_fee + canadian_dollars + monthly_gas_transaction_fee) * (1 + tax_rate)
print("Thank you! Your total amount due now is: " + "$" + str(round(total, 2)))
