#-*- coding:utf-8 -*-

import MyPen
import MyUtil
from advance.MyUtil import Messenger

MyPen.write()
print MyPen.name

m1=MyUtil.Messenger()
m1.sendMessage('hello~')

m2=Messenger()
m2.sendMessage('okay!')