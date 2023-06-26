"""스텐드얼로운(standalone) 프로그램
지금까지는 파이썬의 대화식 인터페이스에서 코드를 작성하고 실행했다.
이번에 만들 파이썬 프로램은 <<< 가 존재하지 않는다.
실행하기위해서는 터미널 창에서 다음과 같이 입력하면 된다.
$ python standalon.py"""

print("this standalon program works!")

import sys
print('Program argument:', sys.argv)

"""모듈(module), Import문
파이썬에는 계층구조(Hierarchy)가 존재한다.
상향식구조로 
단어:데이터 타입(data type)
문장:선언문(statement)
단락:함수(function)
장:모듈(module)
"""

"""이번에는 import문을 사용하여 다른 모듈을 참조하는 방법을 배워볼 것이다.
import한 모듈은 해당 파일 내에 있는 코드와 변수를 사용할 수 있게 만들어 준다."""

#ex) wetherman.py와 report.py파일을 만들어준다.
# 이 예제는 random에서 choice를 불러냈고 weatherman.py는 report.py파일을 불러왔다.
""" report.py
def get_description():
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
"""

""" weatherman.py
import report
description = report.get_description()
print("To day's weather:", description)
"""
"""결과
D:\파이썬>python weatherman.py
To day's weather: sleet

D:\파이썬>python weatherman.py
To day's weather: who knows"""

# 같은 import를 반복해서 사용하는 경우 함수내에서 쓰기보다는 밖으로 내보내는 것이
# 효율적일 수 있다. 

# Tip1 모듈의 이름을 바꾸고 싶거나 줄여서 사용하고 싶을때 
# [import (모듈) as (바꿀이름)]으로 작성하면 간편하게 작업할수 있다.
"""
import turtle as t
for i in range(35):
    t.forward(1)
    t.backward(1)"""

# Tip2 큰 모듈안에서 필요한 부분만 import 하기위해서는 
# [from (모듈) import (필요한 부분)]식으로 작성하면 된다.
"""
from report import get_description
description = get_description()
print("Today's weather:", description)"""

"""파이썬은 import할 파일을 어디에서 찾을까?
디렉터리 이름의 리스트와 표준 sys모듈에 저장되어있는 ZIP파일을 변수 path로 사용한다.
이 리스트에 접근해서 경로를 수정할 수 있다."""

import sys
for place in sys.path:
    print(place) 
"""
C:\Users\genen\AppData\Local\Programs\Python\Python311\Lib\idlelib
C:\Users\genen\AppData\Local\Programs\Python\Python311\python311.zip
C:\Users\genen\AppData\Local\Programs\Python\Python311\Lib
C:\Users\genen\AppData\Local\Programs\Python\Python311\DLLs
C:\Users\genen\AppData\Local\Programs\Python\Python311
C:\Users\genen\AppData\Local\Programs\Python\Python311\Lib\site-packages"""

# 만약 표준 라이브러리와 중복된 모듈이 존재한다면 현재 디렉토리에서 먼저 찾기 때문에 표준 라이브러리에서 import할 수 없다.