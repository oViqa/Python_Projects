# global constant : a variable defined at the module level (outside of any function or class) 
# that is intended to hold a value that should not change throughout the program's execution.
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value= {
    "A" : 6,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
    
def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for sym, count in symbols.items():  # key + value in the dictionnary
        for _ in range(count):  # anonymous variable "_" used when you do not need the iteration index
            all_symbols.append(sym)
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]  # copy so original list doesn't change
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()
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

#  find out the bet and then multiply it by the amount
def get_number_of_lines():
    while True:
        # string concatenation
        # Using f-string (Python 3.6+)
        # lines = input("Enter the number of lines to bet on (1-{})?".format(MAX_LINES))
        # lines = input("Enter the number of lines to bet on (1-%d)?" % MAX_LINES)
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})?\n")
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
    global spin_count
    try:
        spin_count
    except NameError:
        spin_count = 0
    spin_count += 1
    print(f"Spin: {spin_count} | Current balance: ${balance}")
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${bet * lines}")
    slots = get_slot_machine_spins(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    balance += winnings - total_bet
    print(f"You won ${winnings}.")
    if winning_lines:
        print("You won on lines:", ", ".join(map(str, winning_lines)))
main()