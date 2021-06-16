# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 11:52

import configparser
import time

from airtest.core.android.adb import ADB


'''
公共工具文件，包含了该自动化的公共函数
'''

def deList():
    #返回当前设备连接UUID
    deviceName = []
    connectDevices = ADB().devices('device')
    deviceslist = [i[0] for i in connectDevices]
    return deviceslist

def loadini():
    #读取设备配置ini文件
    try:
        cg = configparser.ConfigParser()
        cg.read('deviceList.ini')
        #print(cg.items)
        section_list = cg.items('device')
    except Exception:
        print('读取手机配置文件deviceList.ini出错')
        raise Exception
    return section_list


def checkDevice():
    #将设备保存为 dict
    deviceName = []
    deviceslist =deList()
    section_list = loadini()
    dct = dict(section_list)
    #翻转 dict
    new_dict = {v : k for k, v in dct.items()}
    dctValues = list(dct.values())
    for i in deviceslist:
        for j in dctValues:
            if i in j:
                deviceName.append(new_dict[i])
    settle = []
    for n in deviceName:
        if n != 'huawei' and 'yyting':
            settle.append(n + 'pro')
        else:
            settle.append(n)
    return settle,new_dict


def timeout(sum):
    #sum = 10 设置倒计时时间
    timeflush = 0.25  # 设置屏幕刷新的间隔时间
    for i in range(0, int(sum/timeflush)):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r请稍等 {}".format(list[index]), end="")
        time.sleep(timeflush)

