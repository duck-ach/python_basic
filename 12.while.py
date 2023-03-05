# 카페에 손님이 일정시간 이상 나타나지않으면 커피를 폐기함

customer = "토르"
index = 5
while index >= 1 : 
    print("{0}님, 커피가 준비되었습니다. {1}분 남았어요.".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기 처분 되었습니다.")
        
'''
# 무한루프     
customer = "아이언맨"
while True :
    print("{0}님, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
'''  

'''
# 손님이 토르일때까지 무한루프
person = "Unknown"
while person != customer :
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
'''

