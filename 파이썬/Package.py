"""파이썬 애플리케이션을 조금더 확장가능하게 만드는 모듈을 패키지(Package)라고 한다.
패키지는 파일 상층구조에 구성한다."""

# ex) daily.py and weekly.py

"""daily.py
def forcast():
    'fake weekly forcast'
    return 'like yesterday'
"""

"""weekly.py
def forecast():
    "Fake weekly forecast"
    return ['snow', 'more snow', 'sleet',
            'freezing', 'rain', 'fog', 'hail']
"""

# 메인 프로그램 weather.py
from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

"""results
PS D:\파이썬\sources> cd D:\파이썬        
PS D:\파이썬> python Package.py
Daily forecast: like yesterday
Weekly forecast:
1 snow
2 more snow
3 sleet
4 freezing
5 rain
6 fog
7 hail"""