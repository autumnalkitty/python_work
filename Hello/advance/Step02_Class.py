#-*- coding:utf-8 -*-

'''
[class 정의하기]
'''
class Car:
    #필드 정의하기
    name=u'소나타'
    
    #객체를 생성할 때 호출되는 생성자
    def __init__(self):
        print u"Car 클래스의 생성자 호출"
    
    #메소드 정의하기
    def drive(self): #this 예약어가 없는 대신 self 가 비슷한 역할을 수행
        print u"달려요!"
    
    def showInfo(self):
        print 'self.name:', self.name
#Car class 를 이용해서 객체 생성하기
c1=Car()
c1.drive()
print c1.name
c1.showInfo()