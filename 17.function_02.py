
'''
# 값을 전달해주는 함수(매개변수)
16.function_01.py에 있는 내용과 같이 값을 전달하지 않는 함수도 있고, 매개변수를 전달하는 함수도 있다.
'''
def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money) : # 출금
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("계좌에 잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 밤에 출금(수수료가 붙음)
    commission = balance * 0.1 # 수수료 0.1%
    if balance >= (money + commission) :
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money - commission))
        return balance - (money + commission)
    else:
        print("계좌에 잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
    

balance = 0 # 잔액
balance = deposit(balance, 1000)  # 입금이 완료되었습니다. 잔액은 1000원 입니다.
balance = withdraw(balance, 2000) # 계좌에 잔액이 부족합니다. 잔액은 1000원 입니다.
balance = withdraw(balance, 500)  # 출금이 완료되었습니다. 잔액은 500원 입니다.
balance = deposit(balance, 5000)
balance = withdraw_night(balance, 1000)
