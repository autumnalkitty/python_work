#-*- coding:utf-8 -*-

'''
[math]
'''
import math #수학에 관련된 module 을 제공하는 package

#원의 넓이 구하기
r=input(u'원의 반지름 입력: ')
area=3.14*r*r
area2=math.pi*r**2
area3=math.pi*math.pow(r, 2)
print area, area2, area3

num=1234.5678
result1=math.floor(num) #내림
result2=math.ceil(num) #올림
result3=round(num) #반올림
print result1, result2, result3
