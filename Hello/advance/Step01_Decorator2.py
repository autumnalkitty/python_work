#-*- coding:utf-8 -*-

'''
[decorator]
함수의 장식자
@decorator_name
'''
#decorator 로 사용할 함수 정의
def helloBye(func):
    #인자로 전달된 func 는 함수의 참조값
    def wrapper():
        print "hello!"
        func() #인자로 전달된 함수 호출
        print "bye~"
    return wrapper #함수의 참조값 리턴

@helloBye
def f1():
    print u"f1() 수행 완료"
@helloBye
def f2():
    print u"f2() 수행 완료"
@helloBye
def f3():
    print u"f3() 수행 완료"

f1()
f2()
f3()
