# -*- coding:utf-8 -*-

nameSet={'kim','park','lee'}

# set 에 'kim' 의 존재 여부
result1= 'kim' in nameSet

# set 에 'kim' 의 부존재 여부 
result2= 'kim' not in nameSet

print "result1:", result1
print "result2:", result2

# list 에서 중복을 제거할 때 사용할수 있다.
nums=[10,10,20,20,30,30,40,50]

# built-in set class 를 이용해서 중복값이 제거된 set 얻어내기 
set1=set(nums) #set 객체 생성
print set1

# built-in list 클래스를 이용해서 set 를 list 로 얻어내기 
nums2=list(set1)
print "nums2:", nums2

# 정렬
nums2.sort(reverse=True)
print "정렬 후 nums2:"
print nums2