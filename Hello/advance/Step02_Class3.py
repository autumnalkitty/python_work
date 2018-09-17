#-*- coding:utf-8 -*-

'''
Created on 2018. 9. 17.

@author: autumnalkitty
'''
from advance.MyUtil import Messenger

if __name__ == '__main__':
    #Messenger 객체 생성해서 메소드 호출 테스트
    m1=Messenger()
    m1.sendMessage(u'안녕하세요')