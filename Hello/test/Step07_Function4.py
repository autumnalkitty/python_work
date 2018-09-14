#-*- coding:utf-8 -*-

'''
[keyword 인자 전달]
'''
def test1(num, name, addr):
    print num, name, addr
test1(1, u'김구라', u'노량진')
test1(name=u'해골', num=2, addr=u'행신동')

def test2(num=0, name=u'누구게', addr=u'어디게'):
    print num, name, addr
test2()
test2(name=u'원숭이')
test2(num=3, addr=u'동물원')