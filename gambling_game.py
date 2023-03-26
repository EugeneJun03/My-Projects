import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # _를 사용하면 변수를 사용하지 않고 반복문을 실행시킬 수 있다.
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] # 두 개의 리스트가 하나의 저장위치를 공유하지 않게 하기위해서 뒤에[:]를 붙여 주어야 한다.
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns): #이 함수는 가로로 출력되는 슬롯 머신을 세로로 출력되게 변환시켜주는 함수이다.
    for row in range(len(columns[0])):
        for i, colunm in enumerate(columns): # enumerate는 각 개체의 시퀀스 값과 그 자체의 값을 반환해주는 함수이다.
            if i != len(columns) - 1:
                print(colunm[row], end=" | ")
            else:
                print(colunm[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to diposit? $:")
        if amount.isdigit(): # is.digit()은 입력받은 값이 숫자인지 판별해 준다.
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit(): # is.digit()은 입력받은 값이 숫자인지 판별해 준다.
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $:")
        if amount.isdigit(): # is.digit()은 입력받은 값이 숫자인지 판별해 준다.
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")
        else:
            break
    print(f"your are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()