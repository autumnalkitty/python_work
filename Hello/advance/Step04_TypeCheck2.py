#-*- coding:utf-8 -*-
import types

#클래스
class Flower:
    pass

class Rose(Flower):
    pass

class Tulip(Flower):
    pass 

#함수
def myFunction():
    pass

if __name__ == '__main__':
    f1=Flower()
    f2=Rose()
    f3=Tulip()
    
    if isinstance(f1, Flower):
        print u"f1 은 Flower type 입니다."
    if isinstance(f2, Flower):
        print u"f2 는 Flower type 입니다."
    if isinstance(f2, Rose):
        print u"f2 는 Rose type 입니다."
    if isinstance(f3, Flower):
        print u"f3 는 Flower type 입니다."
    if isinstance(f3, Tulip):
        print u"f3 는 Tulip type 입니다."
        
    if isinstance(myFunction, types.FunctionType):
        print u"myFunction 은 function type 입니다."
        
    #클래스의 참조값을 변수에 대입
    gura=Flower
    
    if isinstance(gura, types.ClassType):
        print u"gura 는 class type 입니다."