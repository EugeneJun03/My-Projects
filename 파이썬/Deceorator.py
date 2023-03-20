"""데커레이터(Decorator) - 소스 코드를 바꾸지 않고 함수를 수정해야할 때 
일반적으로는 함수에 전달된 인자를 보기위해 디버깅문을 추가하는 것이다.
하지만 데커레이터는 하나의 함수를 취해서 또다른 함수를 반환하는 함수이다.
사용되는 요소:
    1. *arg와 **kwarg
    2. 내부함수
    3. 함수인자
"""
#ex) document_it()
#1.함수 이름과 인자값을 출력한다.
#2.인자로 함수를 실행힌다.
#3.결과를 출력한다.
#4.수정된 함수를 사용할 수 있도록 반환한다.
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running funtion:', func.__name__)
        print('Positional arguments:', args)
        print ('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
#사용법
def add_ints(a, b):
    return a+b
"""
>>> add_ints(3, 5)
8
>>> cooler_add_int = document_it(add_ints) 
>>> cooler_add_int(3,5)
Running funtion: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8"""
#자동으로 데커레이터 사용하기
"""
>>> @document_it 
... def add_ints(a, b):
...     return a + b
>>> add_ints(3,5) 
Running funtion: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8"""
