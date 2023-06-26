#파이썬의 코드를 반복해서 입력해야하는 더 큰 코드가 필요할경우 함수를 사용한다.
#함수는 기본적으로 매개변수를 통해 반환값을 산출하는 구조로 이루어져있다.

"""1번 정의하기(define:def)
>>> def 함수이름(매개변수):
로 기본적인 구조를 이룬다.
ex)1
>>> def make_a_sound():
        print('quack')
>>> make_a_quack()
quack
ex)2
>>> def agree():
        return True
>>> if agree():
        print('Splendid')
    else:
        print('That was unexpected')
Splendid
ex)3
>>> def eco(something):
        return something + ' ' + something
>>> eco('HELLO')
HELLO HELLO"""

'------------------------------------------------------------------------------'

"""2번 위치인자(Positional Arguments)
>>> def menu(wine, entree, dessert):
        return {'wine':wine, 'entree':entree, 'dessert':dessert}
>>> menu('chardonnay', 'chicken', 'cake')
{'wine':'chardonnay', 'entree':'chicken', 'dessert':'cake'}"""

'-------------------------------------------------------------------------------'

"""3번 키워드 인자(위치인자와 섞어서 사용할수도 있다.)
>>> menu(entree='beef', dessert='bagel', wine='bordeaux') 
{'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}"""
# 만약 키워드인자와 위치인자를 같이 사용할 때에는 위차안자가 먼저 등장해야한다.
# 함수정의 과정에서 키워드 인자를 사용하면 기본 매개변수롤 지정되어 입력하지않으면 그 값이 출력된다.
def work(arg):
    result = []
    result.append(arg)
    return result

def works(arg, result=[]):
    result.append(arg)
    print(result)
    
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

'------------------------------------------------------------------------------'

"""+1 위치인자 모으기(애스터리스크:*)"""
#에더리스크는 매개변수에서 위치 인자 변수들을 튜플로 묵는다.
#*를 사용할 때 args를 사용할 필요는 없지만 관용적으로 사용한다.
#ex)2
def print_args(*args):
    print('Positional argument tuple:', args)
"""
>>> print_args()
Positional argument tuple: ()
>>> print_args(3, 2, 1, 'wait', 'uh...') 
Positional argument tuple: (3, 2, 1, 'wait', 'uh...')"""
#ex)2
def print_more(required1, required2, *arg):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', *arg)
"""
>>> print_more('cap', 'gloves', 'scarf', 'monocle', 'wax')
Need this one: cap
Need this one too: gloves
All the results: scarf monocle wax"""

'------------------------------------------------------------------------------'

"""+2 키워드 인자 모으기(더블 에더리스크:**)"""
#키워드인자를 딕셔너리로 묶기 위해서는 더블 에더리스크를 사용해야한다.
def print_kwargs(**kwarg):
    print('keyword arguments:', kwarg)
"""
>>> print_kwargs(wine='melot', entree='mutton', dessert='macaroon')
keyword arguments: {'wine': 'melot', 'entree': 'mutton', 'dessert': 'macaroon'}"""
#매개변수와 마찬가지로 *arg, **kwarg를 같이 사용하려면 이들을 순서대로 배치해야한다.

#추가적인 스킬 "Docstring" - 함수의 몸체 시작 부분에 문서를 붙여서 함수의 정의를 보충설명해 줄 수 있댜.
#ex)1
def echo(any):
    'echo reterns its input argument'
    return any
"""
#help()를 사용하면 함수내에 서식화된 docstring를 읽어준다.
>>> help(echo)
Help on function echo in module __main__:

echo(any)
    echo reterns its input argument
>>> print(echo.__doc__)
echo reterns its input argument"""

#ex)2
def print_if_true(thing, check):
    """
    Prints the first argument if a sexond argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    """
    if check:
        print(thing)
"""
>>> help(print_if_true)
Help on function print_if_true in module __main__:

print_if_true(thing, check)
    Prints the first argument if a sexond argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument."""

'------------------------------------------------------------------------------'

"""5번 내부함수 - 내부함수는 루프나 중복을 피하기 위해 또다른 함수 내에 
어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 사용된다."""
#ex)1
def outer(a, b):
    def inner(c,d):
        return c+d
    return inner(a,b)
"""
>>> outer(4, 7)
11"""
#ex)2
def knights(saying):
    def inner(quote):
        return "We are the knights who say:'%s'" %quote
    return inner(saying)
"""
>>> knights("Hooo") 
"We are the knights who say:'Hooo'" """

'------------------------------------------------------------------------------'

"""6번 클로저(Closure) - 내부함수는 클로저처럼 행동할수 있다. 클로저는 다른 함수에 의해 동적으로 생성된다.
그리고 바깥 함수로 부터 생성된 변수값을 변경하고 저장할 수 있는 함수이다."""
# 예제는 위의 knights함수를 차용할 것이다.
def knight2(saying):
    def inner2():
        return "We are the knight who say: '%s'" %saying
    return inner2
"""
>>> a = knight2('dd')
>>> b = kinght2("de")
>>> type(a)
<class 'function'>

>>> a
<function knight2.<locals>.inner2 at 0x0000019352385BC0>
>>> a()
"We are the knight who say: 'dd'"
"""

'------------------------------------------------------------------------------'

"""익명 함수(lambda) - 파이썬의 람다함수는 단일문으로 표현되는 익명함수이다."""
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thus', 'meow', 'thud', 'hiss']

def eliven(word):
    return word.capitalize() + '!'
"""
>>> edit_story(stairs, eliven)
Thus!
Meow!
Thud!
Hiss!"""