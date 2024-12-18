#------------------------------------------------#
# Project Title: Bank Balance
# Date (Started): 7/6/2024
# Date (Finished): 7/8/2024
# File Description: Function definitions for
#                   bank balance program
# Author: Ivan Wong
#------------------------------------------------#

#------------------------------------------------#
# Description:
# Prints the options available to the user
#
# Assuming:
# User has not selected an option yet
#
# Output:
# Prints options as a string to the terminal
#------------------------------------------------#
def displayOptions():
    print("\nSelect an Option\n"
          "  1. Show Balance\n"
          "  2. Deposit Amount\n"
          "  3. Withdraw Amount\n"
          "  4. Show Transaction History\n"
          "  5. Exit Program\n")
    
    return


#------------------------------------------------#
# Description:
# Prints the running balance for the bank 
# account
#
# Assuming:
# Program has been run
#
# Output:
# Prints the running balance to the terminal
#------------------------------------------------#
def showBal(balance):
    print(f"Your balance is: ${balance:.2f}")

    return 0


#------------------------------------------------#
# Description:
# Asks user for deposit amount and updates
# the  running balance
#
# Assuming:
# User selected deposit option
#
# Output:
# Updates running balance with amount from 
# the user
#------------------------------------------------#
def deposit(balance, transactions):
    #Error handling
    try:
        #Ask user for amount
        amount = float(input("Enter Amount to Deposit: "))

        #Check if amount is GT 0
        if amount > 0:
            #Update balance and transactions
            balance += amount
            transactions.append(f"Deposited: ${amount:.2f}")

            print(f"Deposited: ${amount:.2f}")

            return amount
        else:
            #Amount id LT 0, error message
            print("Value must be more than $0.00")

            return 0

    #Handling invalid inputs
    except:
        print("Invalid Input")

        return 0


#------------------------------------------------#
# Description:
# Asks user for a withdraw amount and updates
# the running balance
#
# Assuming:
# User selected option to withdraw money
#
# Output:
# Updates running balance with amount from 
# the user
#------------------------------------------------#
def withdraw(balance, transactions):
    #Check if balance is LTE 0
    if balance <= 0:
        #Cannot withdraw, error message and return
        print("Insufficient Funds")
        
        return 0
    #Error handling
    try:
        #Ask user for amount
        amount = float(input("Enter Amount to Withdraw: "))

        #Check for valid amount
        if 0 < amount <= balance:
            #Update balance and transactions
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}")

            print(f"Withdrew: ${amount:.2f}")

            return amount
        #Invalid amount, error message
        else:
            print(f"Value Must be within $0.01 and ${balance:.2f}")

            return 0

    #Handling invalid inputs
    except:
        print("Invalid Input")

        return 0


#------------------------------------------------#
# Description:
# Prints the transaction history
#
# Assuming:
# Program is running
#
# Output:
# Transaction history displayed to terminal
#------------------------------------------------#
def showHistory(transactions):
    #Check for any transactions
    if transactions:
        print("Transaction History:")

        #Loop through list, printing each transaction
        for transaction in transactions:
            print(transaction)
    
    #No transactions, error message
    else:
        print("No Previous Transactions Found")

    return


#------------------------------------------------#
# Description:
# Handles user input for choices available to
# the user
#
# Assuming:
# User input is given
#
# Output:
# Option the user selected
#------------------------------------------------#
def handleOptions(balance, transactions, userOption):
    #Match/case to handle options
    match userOption:
        case "1":
            showBal(balance)

        case "2":
            balance += deposit(balance, transactions)

        case "3":
            balance -= withdraw(balance, transactions)

        case "4":
            showHistory(transactions)

        case "5":
            return 0

        #Default case, error message
        case _:
            print("Invalid Input")

    return balance