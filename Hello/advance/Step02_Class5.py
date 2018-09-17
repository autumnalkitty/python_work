#-*- coding:utf-8 -*-

class Robot:
    #참조값으로 메소드를 call 할 수 있도록 설정
    def __call__(self):
        print u"참조값으로 call 을 했습니다."
    
    #객체 자체를 출력할 때 출력할 문자열을 return 할 수 있다.
    def __str__(self):
        return "I'm a robot!"
        
    def walk(self):
        print u"로봇이 걸어요!"

if __name__ == '__main__':
    #Robot 객체를 생성해서 참조값을 r1 에 담기
    r1=Robot()
    r1.walk()
    
    #참조값 자체를 call 하면 __call__() 메소드가 호출된다.
    r1()
    
    #참조값 자체를 출력하면 __str__() 메소드가 호출된다.
    print r1