"""제너레이터(Generator) - 함수의 시퀀스를 생성하는 객체이다.
제너레이터를 활용하면 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
제너레이터의 속성:
    1. 제너레이터는 이터레이터에 대한 데이터의 소스로 활용된다.
    2. 제너레이터는 일반적인 함수와 다르게 마지막으로 호출된 값을 
    기억하고 다음값을 반환한다.
    3. 제너레이터 함수는 return을 반환으로 사용하지 않고
    yield문으로 반환한다."""
# range()함수 만들어 보기
def my_range(first = 0, last = 10, step = 1):
    number = first
    while number < last:
        yield number
        number += step
"""
>>> my_range
<function my_range at 0x0000028B56C18B80>
>>> ranger = my_range(1,5)
>>> ranger
<generator object my_range at 0x0000028B569E51C0>
>>> for i in ranger:
...     print(i)
...
1
2
3
4
"""