# -*- coding:utf-8 -*-

'''
[set]
1. 순서가 부재
2. 중복 비허용
3. 집합(묶음)과 유사
'''
set1={10, 20, 30, 40, 50}

# 데이터 추가하기
set1.add(60)
set1.add(70)

# 중복된 데이터는 삽입 불가
set1.add(70)
set1.add(60)
set1.add(10)

# 저장된 개수는 len() 메소드를 이용
print "len(set1):", len(set1)

set2={60, 70, 80, 90, 100}

# set1 합집합 set2
result1=set1.union(set2)

# set1 교집합 set2
result2=set1.intersection(set2)

# set1 차집합 set2
result3=set1-set2

# 동물의 집합
animalSet={'cat','dog','snake','lion','tiger'}

# 집합에서 특정값 삭제
animalSet.discard('snake')

# .discard() 는 삭제할 데이터가 없으면 무시한다.
animalSet.discard('elephant')

# 삭제하는 방법2
animalSet.remove('cat')

# .remove() 는 삭제할 데이터가 없으면 예외(Except)를 발생 시킨다.
# animalSet.remove('frog')

# 모든 내용 삭제
animalSet.clear()

nameSet={'lee','kim'}
list1=['park','song']
tuple1=('jo', 'nam')

# set 에 list 나 tuple 을 병합시킬 수 있다.
nameSet.update(list1)
nameSet.update(tuple1)
print nameSet

# 반복문 돌면서 모든 값 하나씩 사용해 보기
for tmp in nameSet:
    print tmp