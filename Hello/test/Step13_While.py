#-*- coding:utf-8 -*-

'''
[반복문 while]
'''
count=0
while True: #무한 루프
    count +=1 #count 1씩 증가시키기
    if count==10:
        break
print u"반복문 탈출 count:", count

count=0
while count<10:
    count +=1
print u"반복문 탈출 count:", count