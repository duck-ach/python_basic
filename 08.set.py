# 집합(set)
# 중복이 안되고, 순서가 없다.
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

# 교집합 (자바와 파이썬을 모두 할 수 있는 사람을 출력해보자.)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'유재석'}
print(java.union(python)) #{'양세형', '박명수', '김태호', '유재석'}

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) # {'양세형', '김태호'}

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}

# java를 잊었어요
java.remove("김태호")
print(java) # {'양세형', '유재석'}