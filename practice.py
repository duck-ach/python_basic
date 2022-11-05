#  숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
# 연산도 가능
print(5+3)
print(2*8)
print(3*(3+4))
# 문자형 자료형
print('풍선') # 작은 따옴표 가능
print("나비") # 큰 따옴표도 가능
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9) # 문자형과 계산을 섞어서 출력도 가능
# boolean 자료형(true/false)
print(5 > 10)       # True
print(5 < 10)       # False
print(True)         # True
print(False)        # False
# not 연산도 가능
print(not True)     # False
print(not False)    # True
print(not (5 > 10)) # True

###############################################################
# 변수(Variable)

# 애완동물을 소개해 주세요~
# 변수는 어떤 바뀔 수 있는 데이터를 담아두는 공간
animal = "고양이" # (변수부분만 바꿔서 실행하면 됨)
name = "네로"
age = 3
food = "츄르"
is_adult = age >= 3

print("우리집 " + animal +"의 이름은 " + name +"에요")
# hobby = "공놀이"
# print(name + "는 "+ str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 "+ str(age) , "살이며, " , food , "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))


#################################################################
# 주석처리
'''
여러문장을
주석처리하고 싶을 때는 작은따옴표(') 3개를 붙이면 된다.
'''
# 샵(#)을 입력해도 한줄 처리를 할 수 있다. 단축키 (ctrl + /)

#################################################################
# 문제. 변수를 이용하여 다음 문장을 출력하시오.
'''
    변수명 : station
    변수값 : "사당", "신도림", "인천공항" 순서대로 입력
    출력문장 : XX행 열차가 들어오고 있습니다.
'''

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")