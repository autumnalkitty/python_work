#-*- coding:utf-8 -*-

'''
[**kwargs]
함수에 전달되는 인자를 dict type 으로 받을 수 있다.
'''
def test1(**kwrags):
    print kwrags
test1(num=1)
test1(num=1, name='gura')
test1(num=2, name='monkey', isMan=True)

def test2(*args, **kwargs):
    print "args:", args, "kwargs:", kwargs
test2(10, 20)
test2(num=1, name='gura')
test2(30, 40, num=2, name='monkey')