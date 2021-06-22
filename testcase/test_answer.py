# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/10 18:39

import pytest


from airtest.core.android.adb import ADB
from airtest.core.api import *



def test_answer2(dev):

    dev.start_app('bubei.tingshu')
    assert True  # to see what was printed