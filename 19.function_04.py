# keyword
'''
    함수의 매개변수를 전달할 때 키워드를 직접 적어주어서
    순서를 맞추지 않아도 된다.
'''
def profile(name, age, main_lang) :
    print(name, age, main_lang)
    
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
'''
    유재석 20 파이썬
    김태호 25 자바
'''
