#-*- coding:utf-8 -*-

'''
[함수의 return type]
'''
def test1():
    print "test1()"
r1=test1() #None

def test2():
    print "test2()"
    return
r2=test2() #None

def test3():
    print "test3()"
    return 10
r3=test3() #int type

def test4():
    print "test4()"
    return {'num':999}
r4=test4() #dict type

def test5():
    print "test5()"
    names=['lee', 'kim', 'park']
    return names
r5=test5() #list type

def test6():
    print "test6()"
    def inner(): #함수 안에 만든 함수
        print "inner()"
    return inner #함수의 참조값 return
r6=test6() #function type(호출 가능)
r6()
