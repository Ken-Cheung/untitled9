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
# 获取连接设备SN
#获取配置文件dict
deivcedict = checkDevice()[1]
targetdevice = deList()

def intallAPKpath(panduan):
    name,path = downloadremotefile(panduan)
    fullpaht = path +'/'+ name
    return fullpaht


def installAPK(dev):
    '''
    vivo比较特殊需要判断vivo 还是vivopro. vivo用的是普通微信支付，vivopro用的是vivo钱包
    普通微信通过在appstore中测试，无需在vivo上重复测试
    '''
    currentdev = connect_device('Android:///{}?cap_method=javacap&touch_method=adb'.format(dev)) #可以从main方法传入dev，无需在这里重新连接
    #检查app是否安装，是执行卸载
    applist = currentdev.list_app()
    for i in applist:
        if app == i :
            currentdev.uninstall_app(app)
            print('设备已经安装：>>> ' + app + ' <<< 正在卸载重新安装公测包')
        if appPRO == i:
            currentdev.uninstall_app(appPRO)
            print('设备已经安装：>>> ' + app + ' <<< 正在卸载重新安装公测包')
    #执行安装
    print('未找到测试app，正在进行安装,当前机型：>>> ' + deivcedict[dev])
    install_APK_NAME = intallAPKpath(deivcedict[dev])
    currentdev.install_app(install_APK_NAME)
    # 这里可以再次检查一下app在不在 list再输出成功
    print('安装 >>>' + install_APK_NAME + ' <<< 成功')

#installAPK()
#