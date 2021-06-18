# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 11:52

import configparser
import os
import time

from airtest.core.android.adb import ADB


'''
公共工具文件，包含了该自动化的公共函数
'''


def deList():
    # 返回当前设备连接UUID
    deviceName = []
    connectDevices = ADB().devices('device')
    deviceslist = [i[0] for i in connectDevices]
    return deviceslist


def loadini():
    # 读取设备配置ini文件
    try:
        cg = configparser.ConfigParser()
        cg.read('device.ini')
        # print(cg.items)
        section_list = cg.items('device')
    except Exception:
        print('读取手机配置文件deviceList.ini出错')
        raise Exception
    return section_list


def checkDevice():
    # 将设备保存为 dict
    deviceName = []
    deviceslist = deList()
    section_list = loadini()
    dct = dict(section_list)
    # 翻转dict
    new_dict = {v: k for k, v in dct.items()}
    # 不在配置文件中的设备统统设定为Others的型号，安装App Store版本
    for i in deviceslist:
        if i not in new_dict:
            dct['other'] = '{}'.format(i)
            new_dict['{}'.format(i)] = 'other'
    dctValues = list(dct.values())
    for i in deviceslist:
        for j in dctValues:
            if i in j:
                deviceName.append(new_dict[i])
    settle = []
    for n in deviceName:
        print(n)
        # if n != 'huawei' and n != 'yyting' and n != 'other':
        #     settle.append(n + 'pro')
        # else:
        settle.append(n)
    return settle,new_dict
    # print(settle, "\n", new_dict)
# checkDevice()


def timeout(sum):
    # sum = 10 设置倒计时时间
    timeflush = 0.25  # 设置屏幕刷新的间隔时间
    for i in range(0, int(sum/timeflush)):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r请稍等 {}".format(list[index]), end="")
        time.sleep(timeflush)


def deleteLoaclApkFiles():
    # 删除apk文件夹下的apk文件
    dirPath = os.getcwd()
    dirPath = os.path.join(dirPath,'apk')
    for root, dirs, files in os.walk(dirPath):
        for i in files:
            baseroot = os.path.join(os.getcwd(),'apk')
            file = os.path.join(baseroot,"{}".format(i))
            os.remove(file)