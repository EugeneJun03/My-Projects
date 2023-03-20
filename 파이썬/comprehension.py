# 컴프리헨션(comprehension)은 자료형을 아주 콤펙트하게 만드는 파이써니한 방법이다.
# 즉, 초급이상의 파이썬을 사용한다고 볼 수 있다.

"""리스트 컴프리헨션(for, if)
>>> number_list = [number for number in range(1,6)]
[1, 2, 3, 4, 5]

>>> number_list2 = [number-1 for number in range(1,6)]
[0, 1, 2, 3, 4]

>>> a_list = [number for number in range(1,6) if number % 2 ==1]
[1, 3, 5]

>>> rows = range(1,4)
>>> cols = range(1,4)
>>> cells = [(row, col) for row in rows for col in cols]
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>> for cell in cells:
        print(cell)
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
>>> for row, col in cells:
        print(row, col)
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
"""

'------------------------------------------------------------------------------'

"""딕셔너리 컴프리헨션(for)
>>> word = 'letters'
>>> letter_count = {letter: word.count(letter) for letter in word}
{'l': 1, 'e': 2, 't': 2, 'r': 1}
>>> letter_count = {letter: word.count(letter) for letter in set(word)}
{'r': 1, 't': 2, 'e': 2, 'l': 1}
""" #set()은 문자열을 정렬시킨다.

'------------------------------------------------------------------------------'

"""셋 컴프리헨션(for)
>>> a_set = {number for number in range(1,6) if number % 3 == 1}
{1, 4}"""

'------------------------------------------------------------------------------'

#튜플은 컴리헨션이 없다! 그러므로 []를 ()로 바꾸어 사용했을떄 작동이 되어도 
#그건 튜플이 아니다. ()안의 내용은 제너레이터 컴프리 헨션이다.
#제너레이터는 한번만 실행될수 있고 실행된 이후에는 삭제된다.

"""제너레이터 컴프리헨션(튜플이 아님!)
>>> number_thing = (number for number in range(1,6))
>>> type(number_thing)
<class 'generator'>
>>> for number in number_thing:
        print(number)
1
2
3
4
5
"""

'------------------------------------------------------------------------------'

"""추가젹인 스킬(zip) 
zip은 여러 시퀀스를 병렬로 순회시켜서 결과 값을 준다."""
days = ['Monday', 'Tuesday', 'Wednesday']
frits = ['Banana', 'Orange', 'Peach']
drinks = ['Coffee', 'Tea', 'Beer']
desserts = ['tiramisu', 'ice cream', 'pie']
for day, frit, drink, dessert in zip(days, frits, drinks, desserts):
    print(day, ": drink", drink, "-eat", frit, "-enjoy", dessert)
"""
Monday : drink Coffee -eat Banana -enjoy tiramisu
Tuesday : drink Tea -eat Orange -enjoy ice cream
Wednesday : drink Beer -eat Peach -enjoy pie"""