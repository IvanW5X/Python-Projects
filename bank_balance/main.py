#------------------------------------------------#
# Project Title: Bank Balance
# Date (Started): 7/6/2024
# Date (Finished): 7/8/2024
# File Description: Main/driver file for bank
#                   balance program
# Author: Ivan Wong
#------------------------------------------------#

#Import file with function definitions
import bank_bal as bank

def main():
    #Declare vars
    balance = 0
    userOption = ""
    transactions = []

    #Print intro
    print("\n"
            "----------------------------------------\n"
            "Welcome, this is a bank balance program\n"
            "----------------------------------------")

    #Keep user in program until they exit
    while userOption != "5":
        bank.displayOptions()

        #Get option from user
        userOption = str(input("Your Choice: "))

        #Update balance after each options
        balance = bank.handleOptions(balance, transactions, userOption)
    
    return

#Run program if main found in name
if __name__ == "__main__":
    main()