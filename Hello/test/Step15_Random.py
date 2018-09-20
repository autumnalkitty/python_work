# -*- coding:utf-8 -*-

'''
[random package 사용하기]
'''
import random as ran

ranNum=ran.random() # 0이상 1미만의 무작위 실수
ranNum2=int(ran.random()*10) # 0이상 10미만의 무작위 정수
ranNum3=int(ran.random()*10)+10 # 10이상 20미만의 무작위 정수
ranNum4=int(ran.random()*45)+1 # 1이상 45 미만의 무작위 정수
ranNum5=ran.randint(1, 45) #1 이상 45미만의 무작위 정수
print ranNum, ranNum2, ranNum3, ranNum4, ranNum5

nums=set()
while True:
    lottoNum=ran.randint(1, 45)
    nums.add(lottoNum)
    if len(nums)==6:
        break
lottoList=list(nums)
lottoList.sort() # 오름차순 정렬
# 내림차순 정렬 lottoList.sort(reverse:True)
print lottoList