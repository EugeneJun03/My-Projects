# try와 error구문은 안의 내용을 실행해보고 아니면 exept 조건에 부합하는 것에 한해서 또 프로그램을 실행한다.

try:
    x = int(input("What's x? "))
    print(f'x is {x}')
except ValueError:
    print("x is not a integer")

"""
What's x? 13
x is 13

What's x? cat
x is not a integer
"""

#else can be used in try-exception statement
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a integer")
else:
    print(f'x is {x}')

# you can ues pass to avoid mentioning the error
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            pass
        else:
            break
    print(f'x is {x}')
get_int()