# 더하기, 빼기, 곱하기, 나누기
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

# 제곱
print(2**3) # 2^3 = 8

## 나머지구하기
print(5%3) # 2
print(10%3) # 1
# 몫 구하기
print(5//3) # 1
print(10//3) # 3

# 비교연산자
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True
# 앞과 뒤의 값이 똑같다
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True
# 앞과 뒤의 값이 같지 않다.
print(1 != 3) # True
print(not(1 != 3)) # False

# 모두 True 일 경우 True
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5))   # True
# 한개만 True일 경우 True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
# 다항 연산자
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

#######################################################
# 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

# 변수에담기
number = 2 + 3 * 4 # 14
print(number)

number = number + 2 # 16
print(number) # 16

number += 2 # number + 2 = 18
print(number) # 18
number *= 2 # 36
print(number) # 36
# 0으로 나눌 수 없다. (어떤 언어든 마찬가지)
number //= 2 # 18
print(number) # 18.0 # '/'를 하면 몫을 소수점으로 표시해주고, '//'를 하면 몫만 표시
number -= 2 # 16
print(number) # 16
number %= 5 # 1
print(number) # 1

########################################################
# 숫자 처리 함수
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 제곱 4^2 = 16
print(max(5, 12)) # 최대값 12
print(min(5, 12)) # 최소값 5
print(round(3.14)) # 소수점 반올림 3
print(round(4.99)) # 소수점 반올림 5

from math import * # math라이브러리안에 있는 모든 것을 이용하겠다.
print(floor(4.99)) # 소수점 내리기 4
print(ceil(3.14))  # 소수점 올리기 4
print(sqrt(16))    # 제곱근 4

#########################################################
# 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성


# 로또값 (1 ~ 45)
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 60 미만의 임의의 값 생성

# randrange() 함수
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성

# randint() 함수
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

''' 
    문제. 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
    월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
    아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

    조건 1 : 랜덤으로 날짜를 뽑아야함
    조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
    조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

    (출력문 예제)
    오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
from random import *

date = int(random() * 28) + 4
print("오프라인 스터디 모임 날짜는 매월 ", str(date),"일로 선정되었습니다.")
date = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 ", str(date), "일로 선정되었습니다.")
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ", str(date), "일로 선정되었습니다.")