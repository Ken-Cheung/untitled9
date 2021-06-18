# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 11:48

from airtest.core.android.adb import ADB
from airtest.core.api import connect_device
from ftpdownlaod import downloadremotefile
from utils import *


'''
逐个切换当前连接的手机去安装下载好的文件
先获取手机列表，再根据文件名匹配机型去安装
'''


app = 'bubei.tingshu'
appPRO = 'bubei.tingshu.pro'
# 获取连接设备SN,获取配置文件dict
deivcedict = checkDevice()[1]
targetdevice = deList()


def intallAPKpath(panduan):
    name, path = downloadremotefile(panduan)
    fullpaht = path + '/' + name
    return fullpaht


def uninstall(currentDevice,applist):
    #先检查在不在，再删除，不然会报错
    for x in applist:
        print(x)
        if x == app:
            currentDevice.uninstall_app(app)
            print('apk文件删除成')
        if x == appPRO :
            currentDevice.uninstall_app(appPRO)


def installAPK(deviceName,currentDevice):
    """
    vivo比较特殊需要判断vivo 还是vivopro. vivo用的是普通微信支付，vivopro用的是vivo钱包
    普通微信通过在appstore中测试，无需在vivo上重复测试
    """
    # 检查app是否安装，是执行卸载
    applist = currentDevice.list_app()
    print(applist)
    print(deviceName)
    uninstall(currentDevice, applist)
    if deviceName == 'huawei':
        # 安装华为
        install_APK_NAME = intallAPKpath(deviceName)
        currentDevice.install_app(install_APK_NAME)
        print('{}'.format(install_APK_NAME)+'   安装完成')
    elif deviceName == 'other':
        # 安装App Store版本
        devicesInsatllPackeges = 'appstore'
        install_APK_NAME = intallAPKpath(devicesInsatllPackeges)
        currentDevice.install_app(install_APK_NAME)
        print('{}'.format(install_APK_NAME) + '   安装完成')
    else:
        # 安装其余的ch_XXX_pay版本
        install_APK_NAME = intallAPKpath(deviceName)
        currentDevice.install_app(install_APK_NAME)
        print('{}'.format(install_APK_NAME)+'   安装完成')


# deviceName = checkDevice()[0]
# devices = deList()
#
# for xDeviceName,yDevices in zip(deviceName,devices):
#     currentDevice = connect_device('Android:///{}'.format(yDevices))
#     installAPK(xDeviceName,currentDevice)