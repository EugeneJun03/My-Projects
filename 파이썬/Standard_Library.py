"""파이썬은 배터리 포함(Batteries included)이라는 철학을 고수하여 유용한 작업을
처리하기위한 많은 표준 라이브러리(Standard library)가 있다.
이 파일에서는 제네릭(generic)를 사용할 수 있는 일부 모듈들을 살펴볼 것이다.
"""

"""1번 누락된 키 처리하기: setdefault(), defaultdict()
- 파이썬에서는 존재하지않는 키로 딕셔너리에 접근하려 하면 예외가 발생한다. 
기본값을 반환하는 get()함수를 활용하면 이예외를 피할 수 있다.
setdefault()함수는 get()함수와 같지만, 키가 누락된 경우 딕셔너리에 항목을 할당시킬 수 있다.
"""
#딕셔너리에 키가 없는 경우 새 값이 사용된다.
'''
>>> periodic_table = {'Hydrogen': 1, 'Helium': 2}
>>> print(periodic_table)
{'Hydrogen': 1, 'Helium': 2}
>>> carbon = periodic_table.setdefault('carbon', 12)
>>> carbon
12
>>> periodic_table
{'Hydrogen': 1, 'Helium': 2, 'carbon': 12}'''

# 존재하는 키에 다른 기본값을 할당하려 하면 키에 대한 원래 값이 반환되고 아무것도 바뀌지 않느다.
'''
>>> carbon = periodic_table.setdefault('carbon', 72)
>>> carbon
12
>>> periodic_table
{'Hydrogen': 1, 'Helium': 2, 'carbon': 12}'''

"""defultdict()함수는 딕셔너리를 생성할 때 모든 새 키에 대한 기본값을 먼저 지정한다.
이 함수의 인자는 함수이다."""

from collections import defaultdict
periodic_table = defaultdict(int)
#이제 모든 누락된 기본값은 0이댜.
periodic_table['Hydrogen'] = 1
'''
>>> periodic_table['Lead']
0
>>> periodic_table
defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})'''
#defaultdict()의 인자는 값을 누락된 키에 할당하여 반환하는 함수이다.
'ex)1'
from collections import defaultdict
def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
'''
>>> bestiary['A']
'Abominable Snowman'
>>> bestiary['B']
'Basilisk'
>>> bestiary['C']
'Huh?'
'''
# int() = 0
# list() = []
# dict() = {}를 각각 반환한다. 만약 인자를 입력하지 않으면 None으로 설정된다.

'+ lamda를 사용해서 인자에 기본값을 설정할 수 있다.'
bestiary = defaultdict(lambda: 'Hola!')
'''
>>> bestiary = defaultdict(lambda: 'Hola!')
>>> bestiary['D']
'Hola!'
'''

'+ defaultdict를 사용하여 카운터 생성하기'
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
'''
>>> for food, count in food_counter.items():
...     print(food, count)
... 
spam 3
eggs 1
'''
#앞의 예제가 일반 딕셔너리였다면 없는 요소를 증가시키려고 
# 할 때마다 예외가 발생하게 된다.

'---------------------------------------------------------------------------'

"""2번 항목 세기 Counter()"""
from collections import Counter
breakfast = ['spam', 'spam', 'egg', 'spam']
breakfast_counter = Counter(breakfast)
'''
>>> breakfast_counter                     
Counter({'spam': 3, 'egg': 1})
'''
# most_common()함수는 모든 요소를 내림차순으로 반환한다. 
# 혹은 숫자를 입력하는 경우, 그 숫자만큼 상위 요소를 반환한다.
'''
>>> breakfast_counter.most_common()
[('spam', 3), ('egg', 1)]
>>> breakfast_counter.most_common(1) 
[('spam', 3)]
>>> breakfast_counter.most_common(2) 
[('spam', 3), ('egg', 1)]
'''
# 카운터를 연산자를 활용해 결합할 수 있다.(+, -, &:교집합, |:합집합)
lunch = ['egg', 'egg', 'bacon']
lunch_counter = Counter(lunch)
'''
>>> lunch_counter                 
Counter({'egg': 2, 'bacon': 1})
>>> breakfast_counter + lunch_counter
Counter({'spam': 3, 'egg': 3, 'bacon': 1})
>>> breakfast_counter - lunch_counter 
Counter({'spam': 3})
>>> lunch_counter - breakfast_counter 
Counter({'egg': 1, 'bacon': 1})
>>> lunch_counter & breakfast_counter 
Counter({'egg': 1})
>>> lunch_counter | breakfast_counter 
Counter({'spam': 3, 'egg': 2, 'bacon': 1})
'''

'---------------------------------------------------------------------------'

"""3번 키 정렬하기: OrderedDict()"""
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk  nyuk!'
    }
for stooge in quotes:
    print(stooge)
'''
Moe
Larry
Curly
'''

# OrderDict()함수는 키의 추가순서를 기억하고, 이터레이터로부터 순서대로 키값을 반환한다.

from collections import OrderedDict
quotes = OrderedDict({
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk  nyuk!'
    })

for stooge in quotes:
    print(stooge)
'''
Moe
Larry
Curly
'''

'---------------------------------------------------------------------------'

"""4번 데크: deque
데크는 스텍과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐다.
-시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때 유용하게 쓰인다."""
#다음 코드는 회문(앞으로 읽으나 뒤로 읽으나 똑같은 단어)인지 확인하는 함수이다.

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
'''
>>> palindrome('a')
True
>>> palindrome('racecar') 
True
>>> palindrome('racecr')  
False
'''

#조금더 간단히게 인덱싱을 사용해 회문인지 확인하는 방법이 있다.
def another_palindrome(word):
    return word == word[::-1]
'''
>>> palindrome('racecar')
True
>>> palindrome('racecr')
False
'''

'---------------------------------------------------------------------------'

"""5번 코드 구조 순회하기: itertools
itertools는 특수 목적의 이터레이터 함수를 포함하고 있다.
for....in 루프에서 이터레이터 함수를 호출할 때 함수는 한번에 한 항목을 반환하고, 호출상태를 기억한다."""

# chain() 함수는 순회가능한 인자들을 하나씩 반환한다.
import itertools
for item in itertools.chain([1,2],['a', 'b']):
    print(item)
'''
1
2
a
b
'''

# cycle() 함수는 인자를 순환하는 무한 이터레이터이다.
import itertools
for item in itertools.cycle([1,2]):
    print(item)
'''
1
2
1
2
1
2
1
....무한히 계속
'''

# accumulate() 함수는 축척된 값을 계산한다. 기본적으로 합계를 계산한다.
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)
'''
1
3
6
10
'''
#operator를 불러들여서 곱셈도 수행할 수 있다. 이외에도 많은 함수들이 존재하니 조합이나 순열을 사용할때 유용하다.
import operator
for item in itertools.accumulate([1,2,3,4], operator.mul):
    print(item)

'---------------------------------------------------------------------------'

"""6번 깔끔하게 출력하기: pprint()"""
from collections import OrderedDict
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk')
])

'''
>>> print(quotes)
OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk')])
'''
# pprint는 프린트를 조금더 체계적으로 정리하여 보여준다.
'''
>>> pprint(quotes) 
OrderedDict([('Moe', 'A wise guy, huh?'),
             ('Larry', 'Ow!'),
             ('Curly', 'Nyuk nyuk')])
'''

'---------------------------------------------------------------------------'

"""7번 요소 출력하기: enumerate()
enumerate는 해당 객체의 내용물과 인덱스를 동시에 알려주는 내장함수이다."""

'''
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]'''

# 함수 정의
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

#사용 예시(gambling_game.py)
def print_slot_machine(columns): #이 함수는 가로로 출력되는 슬롯 머신을 세로로 출력되게 변환시켜주는 함수이다.
    for row in range(len(columns[0])):
        for i, colunm in enumerate(columns): # enumerate는 각 개체의 시퀀스 값과 그 자체의 값을 반환해주는 함수이다.
            if i != len(columns) - 1:
                print(colunm[row], end=" | ")
            else:
                print(colunm[row], end="")
        print()
#즉, columns의 인덱스 값이 i에 저장되고 내용물은 colunm에 대응시켜서 for문으로도 활용할 수 있다.