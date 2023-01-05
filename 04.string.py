sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 오늘 돈까스를 먹었고,
내일은 샐러드를 먹을 생각입니다.
"""
print(sentence3)

####################################
# 슬라이싱
jumin = "990902-2234567"

# 필요한 부분만 잘라서 가져오는것을 슬라이싱(slicing)이라고 한다.
print("성별 : " + jumin[7])
print("태어난 연도 : " + jumin[0:2]) # jumin[n:m] n번째부터 m번째 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지 
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 소문자로
print(python.upper()) # 대문자로
print(python[0].isupper()) # 0번째 글자가 대문자인지 알려주는 것
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # Python이라는 글자를 찾아서 Java로 바꾸기

index = python.index("n")
print(index) # 앞에서부터 1번째로 오는 n을 찾아내기
index = python.index("n", index + 1) 
print(index) # 1번째 index 이후의 n을 찾아내기

print(python.find("Java")) # 원하는 값이 없는 경우 -1 (False 라는 뜻)
print(python.index("Java")) # 원하는 값이 없는 경우 오류가 난다.

print(python.count("n"))

#######################################################
# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1 (%를 이용한 방법)
print("나는 %d살입니다." % 20) # % 뒤에 있는 값을 %d 안에 넣을 수 있다. Demical(정수)타입만
print("나는 %s을 좋아해요." % "파이썬") # Stirng(문자열) 타입만
print("Apple은 %c로 시작해요." % "A") # Charactor(문자) 타입만
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 괄호를 통해 삽입 (순서대로 동작)

# 방법 2 (중괄호를 이용한 방법)
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨강")) # 인덱스를 지정해줄 수 있다.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨강")) # 인덱스를 지정해줄 수 있다.

# 방법 3 (변수처럼 사용)
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age = 20))
# 순서 상관없이 사용가능

# 방법 4 (v3.6 이상~)
age = 20 # 변수를 선언하고,
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f를 먼저 쓰고 적으면, 실제 변수에 담긴 값을 가져다 쓸 수 있다.

################################################################
# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "오리" 입니다.
print("저는 '오리' 입니다.")
print("저는 \"오리\" 입니다.")
print("저는 \'오리\' 입니다.")

# \\ : 문장내에서 \
# 경로를 출력하고 싶다면
# print("c:\\python_basic\\string.py")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 맨 앞으로 이동해서 "Red "를 "Pine"으로 대체

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 문제. 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
'''
    예) http://naver.com
    규칙1 : http://부분은 제외 => naver.com
    규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
    규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                    (nav)               (5)             (1)           (!)
    예) 생성된 비밀번호 : nav51!
'''
site = "http://naver.com"
pwd1 = site[7:10] # nav
spot = site.index(".") # 12
pwd2 = str(len(site[7:spot])) # 5
pwd3 = site.count("e") # 1
password = (pwd1 + str(pwd2) + str(pwd3) + "!")
print(password)
