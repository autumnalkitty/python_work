#-*- coding:utf-8 -*-

#MyUtil.py

print u"MyUtil 의 __name__:", __name__

class Messenger:
    def sendMessage(self, msg):
        print msg, u"를(을) 전송합니다."
        
#main 으로 실행됐을 때(__name__: main)만 실행할 코드
if __name__=='__main__':
    print u"MyUtil.py 가 메인으로 실행됐습니다."