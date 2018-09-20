# -*- coding:utf-8 -*-

'''
[*args]
함수에 여러 개의 인자를 동적으로 전달할 수 있다.
'''
def test1(*args):
    print args # args 는 tuple type
test1()
test1(10)
test1(10, 20)
test1(10, 'kim', True)