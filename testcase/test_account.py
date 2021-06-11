# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 15:12


# 从APP首页跳转到登录页
import time
import pytest
from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def test_accountLogin():
    # 点击一级导航“账号”tab
    start_app('bubei.tingshu')
    time.sleep(6)
    poco("bubei.tingshu:id/home_tabs").child("bubei.tingshu:id/home_tab5").offspring("bubei.tingshu:id/home_tab_image").click()
    time.sleep(3)

    if poco("bubei.tingshu:id/rl_user_info").child("bubei.tingshu:id/user_unlogin_ll").exists():  # 判断账号是否登录，如果找到该控件则表示未登录
        result = True
    else:
        result = False
    stop_app('bubei.tingshu')
    assert result == True

