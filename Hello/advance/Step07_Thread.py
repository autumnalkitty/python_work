#-*- coding:utf-8 -*-

import time
import threading

def printCount(num, name):
    #전달받은 인자 10번 출력하기
    for i in range(10):
        print num, name
        time.sleep(1) #스레드 1초 지연시키기
        print "index:", i
    print "ended printCount()"

if __name__ == '__main__':
    print u"메인 스레드가 시작됐습니다."
    
    #printCount(1, u"김구라")
    #스레드 객체 생성 Thread(target=대상 함수의 참조값, args=함수에 전달할 인자 tuple type)
    t=threading.Thread(target=printCount, args=(1, u"김구라"))
    
    #스레드 시작시키기
    t.start()
    
    t2=threading.Thread(target=printCount, kwargs={'num':2, 'name': u'해골'})
    t2.start()
    
    print u"메인 스레드가 종료됐습니다."