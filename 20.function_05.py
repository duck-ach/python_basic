# 가변인자

'''
    이번에는 친구들이 컴퓨터를 전공하여 할 수 있는 언어가 많다는 가정
    
    # end=" " : print를 끝낼 때 줄바꿈을 하지않고 띄어쓰기로 끝낸다.

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
    
    
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

위와같은 함수구문에서는 유동적이지 못한 단점이 있다.
그래서 항목을 추가할 때에는 함수도 바꿔주어야하고, 빈칸일 경우 ""를 이용하여 다 자릿수를 채워주어야 한다.

'''

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 줄바꿈
    
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")

# 결과 : 할 줄 아는 언어가 몇개이든 출력에 문제가 없다.