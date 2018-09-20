# -*- coding:utf-8 -*-

names=['kim', 'lee', 'park', 'jo', 'choi']

for item in names:
    print item
print '----------'

for i in [0, 1, 2, 3, 4]:
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

for i in range(5):
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

for i in range(len(names)):
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

for i in [4, 3, 2, 1, 0]:
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

for i in range(4, -1, -1):
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

for i in range(len(names)-1, -1, -1):
    tmp=names[i]
    print u'{}: {}'.format(i, tmp)
print '----------'

# ∑100
sum100=0
for item in range(1, 101):
    sum100=sum100+item
print sum100