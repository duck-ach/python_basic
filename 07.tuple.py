# 변경되지 않는 자료형(리스트보다 속도가 빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 튜플은 추가하던지 변경되는 것은 되지않음. 고정적인 값에 적용.
# menu.add("생선까스")

# 이 값을 튜플에 넣어보자.
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 튜플
(name, age, hobby) = ("김종국", 20, "코딩")