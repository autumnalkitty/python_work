# -*- coding:utf-8 -*-

'''
[다중 if 문]
'''
inputNum=input(u'점수 입력: ')
grade=None
if inputNum >= 90:
    grade='A'
elif inputNum >= 80:
    grade='B'
elif inputNum >= 70:
    grade='C'
elif inputNum >= 60:
    grade='D'
else:
    grade='F'
    
print u"입력한 점수 {}점은 {}입니다.".format(inputNum, grade)