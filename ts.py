# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/10 18:39

import multiprocessing
import pytest
import time

from multiprocessing import Queue
from airtest.core.android.adb import ADB
from airtest.core.api import connect_device


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


# def run(devices):
#     '''
#     先对去FTP下载安装包，自动安装，再启动测试
#     :param devices:
#     :return:
#     '''
#     pytest.main(['-q','./testcase/test_account.py::test_accountLogin', '--devices','{}'.format(devices)])
#

if __name__ == '__main__':
    '''
    1.连接每台机器，去ftp目录下载apk文件进行安装
    2.从设备池中获取设备执行测试用例
    3.输出测试报告
    '''
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