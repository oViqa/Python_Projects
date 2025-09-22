# global constant : a variable defined at the module level (outside of any function or class) 
# that is intended to hold a value that should not change throughout the program's execution.

import random
# importing random module to generate random slot machine values
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLLONS = 3
def deposit():
    while True:
        # while loop so that we keep asking for a valid amount until we get one
        amount = input("What would you like to deposit?\n")
        if amount.isdigit():
# is.digit is to tell us if something is a valid number basically
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a valid number")
    return amount

def get_bet():
    while True:
        amount = input("What would you like to bet on each line?\n")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number")
    return amount

# next step is to find out the bet and then multiply it by the amount
def get_number_of_lines():
    while True:
        # string concatenation
        # Using f-string (Python 3.6+)
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})?\n")
        # lines = input("Enter the number of lines to bet on (1-{})?".format(MAX_LINES))
        # lines = input("Enter the number of lines to bet on (1-%d)?" % MAX_LINES)
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be greater than 1 and less than max_lines.")
        else:
            print("Please enter a valid number of lines")
    return lines
# calling deposit // start of the program

def main():
    balance = deposit()
    lines = get_number_of_lines()
    # checking if bet amount is < balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance 
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${bet * lines}")
    print(balance,lines)
main()