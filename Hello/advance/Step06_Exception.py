#-*- coding:utf-8 -*-

'''
[에외 처리]
'''

if __name__ == '__main__':
    try:
        num1=input(u"나눌 수 입력: ")
        num2=input(u"나누어지는 수 입력: ")
        result=num2/num1
        print u'{} 을(를) {} 으로(로) 나눈값은 {}입니다.'.format(num2, num1, result)
    
    except ZeroDivisionError, zde: #exception type, 변수명
        print zde
        print u"어떤 수를 0으로 나눌 수는 없어요!"
    
    print u"메인 스레드가 종료됐습니다."