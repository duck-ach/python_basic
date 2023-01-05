# 리스트 []
# 순서가 있는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명이 있다.
subway1 = 10
subway2 = 20
subway3 = 30
# 위와같은 변수로 처리할 것을 한번에 리스트로 묶어줄 수 있다.


subway = [10, 20, 30]
print(subway)

subway = ["손석구", "류준열", "강동원"]
print(subway)

print(subway[1])
# 류준열씨가 몇 번째 칸에 타고 있는가?
print("류준열씨는 " , subway.index("류준열") + 1 , "번째 칸에 타고 있습니다.")

# 하하씨가 다음 정류장에서 다음 칸에 탐 (추가)
subway.append("김태형")
print(subway)

# 한요한씨를 손석구 / 류준열 사이에 태워봄
subway.insert(1, "한요한")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 (삭제)
subway.pop()
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("손석구")
print(subway)
print(subway.count("손석구"))

# 정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)

# 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["류준열", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)