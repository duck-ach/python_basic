# 사전
# key와 value 형태로 나옴
# key는 중복 x
cabinet = {3:"손석구", 100: "류준열"}
print(cabinet[3]) # key값을 적어주면 된다.
print(cabinet[100])

print(cabinet.get(3))

# key값이 없으면 오류를 발생시키고 그 뒤의 코드를 출력하지 않고 멈춘다.
# print(cabinet[5])
# print("hi")
# 그 대신 .get을 이용하여 값을 가져오면 None을 출력하고 뒤에있는 코드도 출력한다.
print(cabinet.get(5))
print("hi")

# 값이있다면 값을 출력하고, 없다면 "사용가능" 출력
print(cabinet.get(5), "사용가능")

print(3 in cabinet) # 해당 키의 값이 존재하는가? True를 출력한다.
print(7 in cabinet) # False를 출력한다.

cabinet = {"A-3" : "손석구", "B-100" : "마동석"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "기리보이"
cabinet["C-20"] = "한요한"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key와 value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점 (모든 값 삭제)
cabinet.clear() 
print(cabinet)