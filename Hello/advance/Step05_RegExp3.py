#-*- coding:utf-8 -*-

'''
[정규 표현식으로 매칭되는 모든 문자열 찾기]
'''
import re

msg="monday gura tuesday monkey wednesday thursday friday saturday sunday"

if __name__ == '__main__':
    #정규 표현식
    pattern="[a-z]*day"
    result=re.findall(pattern, msg) #result 는 찾은 문자열이 담긴 list type
    print "result:", result
    
    print u"pattern 에 매칭되는 문자열 개수:", len(result)
    print u"--매칭되는 문자열 목록--"
    for tmp in result:
        print tmp