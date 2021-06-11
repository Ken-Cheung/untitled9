# -*- coding:utf-8 -*-
# author: Zzzsy
# @Time : 2021/6/11 10:35

import time
import pytest

from poco.drivers.android.uiautomation import AndroidUiautomationPoco



app = 'bubei.tingshu:id'
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
startMark = '推荐'


def returnToHomePage():
    # 如果顶栏推荐在，则不需要滑动
    # 先判断推荐在不在，再向右滑动
    # 滑动一次判断一下推荐在不在
    while True:
        if not poco("{}/title_container".format(app)).child("android.widget.TextView", text='推荐').exists():
            poco("{}/title_container".format(app)).swipe('right', duration=0.1)
        else:
            print('已经出现了推荐两个字')
            poco("{}/title_container".format(app)).child("android.widget.TextView", text='推荐').click()
            ## double cheak 有时候没有点击跳转正确，需要二次确认
            print('点击回到了首页')
            break
    return True


@pytest.mark.skip()
def test_homePageTopbar():

    '''
    该函数就是对Title进行循环点击，切换到不同的页面。全部点完无报错返回Ture
    把获取到的加入到list，list最后一个还是等于当前的这个，则已经滑动到底
    分类页的hot_channel与首页的"bubei.tingshu:id/title_container"对应
    '''
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    print(x)
    print(y)

    orginlist = []
    try:
        #先进入分类页
        time.sleep(3)
        poco("{}/fl_classify".format(app)).click()
        #分类页有两种展示
        if poco("bubei.tingshu:id/refreshLayout",text='skdujfkjd').child("bubei.tingshu:id/rv").offspring("bubei.tingshu:id/switchSort").exists():
            pass

        else:
            for hot_channelItem in poco("{}/head_hot_channel".format(app)).offspring("{}/sub_recycler_view".format(app)).offspring():
                if hot_channelItem.get_text():
                    orginlist.append(hot_channelItem.get_text())
        #点击离开分类页
        poco("{}/iv_close".format(app)).click()
        #判断是不是在推荐页
        homePage = returnToHomePage()
        if homePage == True:
            for orginListItem in orginlist:
                if orginListItem == startMark:
                    continue
                else:
                    poco(text="{}".format(orginListItem)).click()
                    if poco("{}/progress_view".format(app)).child("{}/loadingTextView").exists():
                        time.sleep(30)
                    #snapshot(filename="{}/{}.jpg".format(snapshotPaht,orginListItem),msg="首页截图",quality=90)
            print('全部点击完毕')
    except Exception as e :
        print(e)
        hometitle_Container = False
    else:
        hometitle_Container = True
    assert hometitle_Container == True