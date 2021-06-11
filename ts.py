# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/10 18:39

import multiprocessing
import pytest
import time

from multiprocessing import Queue
from airtest.core.android.adb import ADB
from airtest.core.api import connect_device

def timeout(sum):
    #sum = 10 设置倒计时时间
    timeflush = 0.25  # 设置屏幕刷新的间隔时间
    for i in range(0, int(sum/timeflush)):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r请稍等 {}".format(list[index]), end="")
        time.sleep(timeflush)

def deList(queue):
    #返回当前设备连接UUID
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
    pytest.main(['-q', './testcase/test_account.py::test_accountLogin', '--devices', '{}'.format(getDevices)])


def run(devices):
    '''
    先对去FTP下载安装包，自动安装，再启动测试
    :param devices:
    :return:
    '''
    pytest.main(['-q','./testcase/test_account.py::test_accountLogin', '--devices','{}'.format(devices)])


if __name__ == '__main__':
    queue = Queue()
    devs = deList(queue)
    pool = []
    for i in devs:
        #dev = connect_device("Android:///" + f'{i}')
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