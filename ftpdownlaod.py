# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 14:48

'''
连接FTP，下载文件
ftpfile 需要从外部传入,测试需要所以写死
'''

import os
from ftplib import FTP

ftpfile='/packet/bubei.tingshu/9.9.9'
host='192.168.2.62'
prot=21
user='audio_tester'
passwd='kc8AXRG1a137'


def connectFtp():
    ftp = FTP()
    try:
        ftp.connect(host, prot)
        ftp.login(user, passwd)
        #print(ftp.getwelcome())
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print('\n+------- ftp connection successful!!! --------+')
    return ftp


def downloadremotefile(deviceModle=None):
    ftp = connectFtp()
    remotelist = []
    #downlist = []
    buffer_size = 10240
    localpath = os.getcwd()
    #print(localpath)
    ftp.cwd(ftpfile)
    try:
        ftp.cwd(ftpfile)
    except:
        raise
    else:
        print('正在切换FTP目录进入：' + ftpfile)
    for ftppnlstFiles in ftp.nlst():
        remotelist.append(ftppnlstFiles)
        #print(remotelist)
    for downloadfilename in remotelist:
        #for deviceModle in targetAPK:
            if deviceModle in downloadfilename:
                #print('正在下载：' + downloadfilename)
                try:
                    with open("{0}/{1}".format(localpath, downloadfilename),"wb") as f:
                        ftp.retrbinary('RETR {0}'.format(downloadfilename),f.write)
                        print('文件下载完成')
                except Exception as e:
                    print(e)
                break
    ftp.close()
    return downloadfilename,localpath