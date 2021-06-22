# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/10 18:39

import multiprocessing
import pytest
import time

from multiprocessing import Queue
from airtest.core.android.adb import ADB
from airtest.core.api import connect_device
from installAPK import installAPK
from utils import checkDevice
from checkSysdialog import *


def deList(queue):
    # 返回当前设备连接UUID
    deviceName = []
    connectDevices = ADB().devices('device')
    deviceslist = [i[0] for i in connectDevices]
    for i in deviceslist:
        queue.put(i)
    return deviceslist


def getList(queue):
    getDevices = queue.get()
    dev = connect_device("Android:///" + f'{getDevices}')
    print(getDevices)
    # 消除所有弹框
    dialog(dev)
    # ./report 目录下面根据不同的机型创建不同的目录，各个机型的测试结果输出到各目录之下
    pytest.main(['-s', '-q', './testcase/test_answer.py::test_answer2', '--devices', '{}'.format(getDevices), "--alluredir=./report/"])


def startUP():
    deviceName = checkDevice()[0]
    devices = deList(queue)
    for xDeviceName, yDevices in zip(deviceName, devices):
        currentDevice = connect_device('Android:///{}'.format(yDevices))
        installAPK(xDeviceName, currentDevice)


if __name__ == '__main__':
    '''
    1.连接每台机器，去ftp目录下载apk文件进行安装
    2.从设备池中获取设备执行测试用例
    3.输出测试报告
    '''
    queue = Queue()
    devs = deList(queue)
    pool = []
    startUP()
    for i in devs:
        dev = connect_device("Android:///" + f'{i}')
        p = multiprocessing.Process(target=getList,args=(queue,))
        p.start()
        time.sleep(2)
        pool.append(p)
    for pool in pool:
        pool.join()

    #异步
    # pool = Pool(len(devs))
    # for i in devs:
    #     dev = connect_device("Android:///" + f'{i}')
    #     pool.apply_async(run(dev))
    #     time.sleep(2)