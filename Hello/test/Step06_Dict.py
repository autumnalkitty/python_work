#-*- coding:utf-8 -*-

'''
[dict type]

1. key:value 형태로 데이터 관리
2. 순서가 부재
3. key 값을 이용해서 저장된 데이터를 참조
'''
dict1={"num":1, "name":"gura", "isMan":True}

#dict1["key"] 형태로 데이터를 참조
a=dict1["num"]
b=dict1["name"]
c=dict1["isMan"]
print "a:", a
print "b:", b
print "c:", c

#dict 에 이쓴 데이터 수정
dict1["num"]=999 #참조한 뒤 대입연산자를 이용해서 값 대입
print "수정 후 dict1['num']:", dict1["num"]

#특정 방 삭제
del dict1["isMan"] #del 예약어와 함께 해당 방 참조

print u"Step06_Dict 가 종료됩니다."