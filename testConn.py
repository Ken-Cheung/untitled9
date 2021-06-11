# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/10 19:11
from airtest.core.api import *

dev = connect_device('Android:///GWY0217824000760')
# auto_setup(__file__,devices=[f"{dev}?cap_method=JAVACAP&&ori_method=ADBORI"])
a = dev.list_app()
print(a)


print('*结束*')

dev2 = connect_device('Android:///721QECSC3ANLS')
a = dev.list_app()
print(a)