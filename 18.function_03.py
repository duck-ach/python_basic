def profile(name, age, main_lang) :
    print("이름 : {0}\t나이 : {1}\t 주 사용언어 : {2}".format(name, age, main_lang))
    
profile("류준열", 20, "자바")
profile("최우식", 25, "파이썬")


# 같은학교 같은학년 같은반 같은수업 (이름만 다르고, 나이나 언어는 같을 것)
''' 
    보통 함수를 호출하면서 전달 받게되는데, 전달받지 않게 될 경우 
    default값으로 age=17과 main_lang="파이썬"을 전달 받음
'''
def ban_profile(name, age=17, main_lang="파이썬") :
    print("이름 : {0}\t나이 : {1}\t 주 사용언어 : {2}".format(name, age, main_lang))

ban_profile("김채원")
ban_profile("사쿠라")