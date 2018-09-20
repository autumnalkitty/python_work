# -*- coding:utf-8 -*-

'''
[입력한 정보를 str type 으로 받기]
'''
result=raw_input(u'문자열 입력: ')
print "type:", type(result)
print "result:", result

# str type 을 unicode type 으로 바꾸기
result2=result.decode('utf-8')
print "result2 type:", type(result2)
print "result2:", result2