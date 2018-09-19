#-*- coding:utf-8 -*-

from pip._vendor import requests #http 요청할 수 있는 요청객체 import
import threading

def getHtml(url):
    #http 요청을 하고 응답객체를 리턴받는다.
    responseObject=requests.get(url)
    
    #응답된 문자열 출력해보기
    print responseObject.text
    
if __name__ == '__main__':
    print u"메인 스레드가 시작됐습니다."
    
    #getHtml("http://daum.net")
    t1=threading.Thread(target=getHtml, args=("http://daum.net",))
    t1.start()
    
    print u"메인 스레드가 종료됐습니다."