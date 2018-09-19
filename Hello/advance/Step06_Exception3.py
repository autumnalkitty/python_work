#-*- coding:utf-8 -*-

'''
[사용자 정의 예외 발생시키기]
프로그래머가 의도하는 시점에 직접 예외를 발생시킬 수 있다.
raise 예외객체
'''

if __name__ == '__main__':
    try:
        msg=input(u"정수 입력: ")
        if not isinstance(msg, int):
            #원하는 시점에 예외 발생시키기
            raise ValueError(u"정수를 입력하세요!")
        print u"입력한 정수:", msg
    
    except ValueError, ve:
        print ve
        
    print u"메인 스레드가 종료됐습니다."