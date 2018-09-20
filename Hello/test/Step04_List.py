# -*- coding:utf-8 -*-

'''
[list type]

1. 순서가 존재(index)
2. 여러 개의 데이터 저장 가능
3. 값의 변경 가능
'''
from pkg_resources._vendor.pyparsing import hexnums
family=[u"엄마", u"아빠", u"나"]

# 데이터 추가
family.append(u"남동생")
family.append(u"여동생")

# 데이터 삭제
del family[3] #by index
family.remove(u"여동생") #by value

# 가장 마지막 방의 내용 가져오기
result=family.pop()

# 데이터 수정
family[0]=u"어머니"

# 데이터 참조
person=family[1]

nums=[10, 20, 30, 40, 50]

# 오름차순 정렬
nums.sort()

# 내림차순 정렬
nums.sort(reverse=True)

# 반복문
for tmp in nums:
    print tmp

# 배열의 방의 개수
size=len(hexnums)
print "size:", size

print u"Step04_List.py 가 종료됩니다."