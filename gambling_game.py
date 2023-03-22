MAX_LINE = 3

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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()