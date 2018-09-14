#-*- coding:utf-8 -*-

'''
[비교 연산자]
1. 숫자 비교
2. 문자열 비교
3. 참조값(id) 비교
4. 동일객체 여부 비교
'''
#숫자의 비교는 동등 비교연산자로 비교(==, !=)
num1=10
num2=20
num3=10

#문자의 비교는 동등 비교연산자로 비교(==, !=)
str1='kim'
str2='lee'

str3='kim'
list1=[10, 20]
list2=[10, 20]
list3=list1

#list type 의 경우 동등 비교연산자는 값을 비교한다.
result1=list1==list2 #True
result2=list2==list3 #True
result3=list3==list1 #True

#list type 의 참조값(id)를 비교하기 위해서는 id() 를 사용해야한다.
result4=id(list1)==id(list2)
result5=id(list2)==id(list3)
result6=id(list3)==id(list1)

#id() 와 동등 비교연산자 대신 is 를 사용할 수도 있다.
result7=list1 is list2
result8=list2 is list3
result9=list3 is list1

print u"Step09_Compare.py 가 종료됩니다."