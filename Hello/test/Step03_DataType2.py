#-*- coding:utf-8 -*-

#list type(변경 가능한 배열)
nums=[10, 20, 30, 40, 50]
names=['kim', 'lee', 'park']
friends=[u'김구라', u'해골', u'원숭이']

#tuple type(변경 불가능한 배열)
nums2=(10, 20, 30, 40, 50)
names2=('kim', 'lee', 'park')
friends2=(u'김구라', u'해골', u'원숭이')

#dict type
mem1={"num":1, "name":u"김구라", "isMan":True}
mem2={"num":2, "name":u"해골", "isMan":False}

#function type
def a():
    pass
def b():
    print 'one'
    print 'two'
    print 'three'
b() #함수 b 호출

#None type
emptyVar=None

#set type(집합}
set1={10, 20, 30, 10, 20}
    
print u"Step03_DataType2.pv 가 종료됩니다."