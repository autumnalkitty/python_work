# -*- coding:utf-8 -*-

'''
[tuple type]

1. list type 의 read only 버전
2. 수정, 삭제 불가
3. list type 보다 빠른 처리 속도
'''
tuple1=(10, 20, 30, 40, 50)

for tmp in tuple1:
    print "tmp:", tmp

# tuple[0]=999 수정 불가

# del tuple1[0] 삭제 불가

# 방 1개짜리 tuple 만들 때
result=(1+1) #int type 2
result2=(1+1,) #tuple type (2)
result3=('kim',) #tuple type ('kim')

# 대입할 때 () 생략가능
result4='kim', 'lee', 'park'

# 여러 개의 변수에 한 번에 값 할당하기
a, b, c=10, 20, 30

# 두 변수에 있는 내용을 상호 교환
first='girl'
second='boy'
first, second-second, first

print u"Step05_Tuple 이 종료됩니다."