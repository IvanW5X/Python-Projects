The bank balance program is a program that simulates a user's bank account.
The user is able to view their balance, deposit money, withdraw money,
view transaction history and exit the program. The goal of this program is
to introduce programmers that do not know Python just yet to become more
familiar with the language.

The user will have options to...
show their current balance,
deposit money,
withdraw money,
view transaction history and
exit the program.

Some additional requirements are that...
the balance must start at 0 at start-up of the program,
depositing a negative amount must produce an error message,
withdrawing a negative amount OR an mount greater than the current
balance must produce an error message,
the user must stay in the program until the user decides to exit and
a seperate main and function definition file must be used (hint,
use import).

Solution/Implementation:
    Updating balance:
    In Python, passing in parameters uses call-by-value, which creates a copy
    of the variable and is deleted once the scope ends. This is not ideal for our
    program, so one solution I used was to create a handleOptions function that has
    all of the options available to the user and returns the balance once the user
    selects and option. Doing it this way also means that my deposit and withdraw
    functions now need to return the amounts presented by the user such that in the
    handleOptions functions, we can update that balance here.
    Storing Previous Transactions:
    Luckily for us, arrays in Python are relatively easy to work with, so in the
    deposit and withdraw function, I decided to store a string of the Transactions
    in an array, so that when the user wants to view their transactions, a simple for-loop
    is used to print each transaction.
    Implementations:
    Please view the Python files for further details of the program, all code is commented
    and neatly written.