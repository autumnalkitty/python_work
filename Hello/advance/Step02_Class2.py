#-*- coding:utf-8 -*-

'''

'''
class Starbucks:
    #생성자
    def __init__(self, branch):
        #필드를 만들면서 인자로 전달되는 값을 저장
        self.branch=branch
    
    #메소드
    def showInfo(self):
        print u"스타벅스 {}점입니다.".format(self.branch)
s1=Starbucks(u'종각')
s1.showInfo()
s2=Starbucks(u'을지로국제빌딩')
s2.showInfo()