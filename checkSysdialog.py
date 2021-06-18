# -*- encoding=utf8 -*-
# __author__ = "chengaoyi"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def dialog(dev):
    # 启动APP
    dev.start_app("bubei.tingshu")
    print("启动APP")
    time.sleep(5)


    '''
    判断用户是否第一次安装打开、关闭各个机型的授权会话框、听吧页各种弹框
    '''
    # 用户协议弹框若存在则点击“同意”
    if poco("bubei.tingshu:id/btn_dialog_right").exists():
        print("用户首次安装打开App！")
        poco("bubei.tingshu:id/btn_dialog_right").click()
        time.sleep(5)

        '''
        各个机型的授权弹框进行授权
        '''
        # vivo X27手机：存储权限，点击“允许”
        if poco("com.android.permissioncontroller:id/dialog_title", text="权限请求").exists():
            poco("com.android.permissioncontroller:id/permission_allow_button", text="允许").click()
            time.sleep(3)
        else:
            pass

        # oppo手机：存储空间权限，点击“允许”
        if poco("com.android.permissioncontroller:id/permission_allow_button1", text="允许").exists():
            poco("com.android.permissioncontroller:id/permission_allow_button1", text="允许").click()
            time.sleep(3)
        else:
            pass

        # 魅蓝note6手机：存储权限，点击“允许”
        if poco("com.android.packageinstaller:id/mz_permission_dialog_item_title", text="手机存储").exists():
            poco("com.android.packageinstaller:id/permission_allow_button", text="允许").click()
            time.sleep(3)
        else:
            pass

        # 华为mate9手机：访问设备的照片、媒体内容和文件权限，点击“允许”
        if poco("com.android.packageinstaller:id/permission_message").exists():
            poco("com.android.packageinstaller:id/permission_allow_button", text="始终允许").click()
            time.sleep(3)
        else:
            pass

        # 华为nova7、华为荣耀9x手机：访问设备的照片、媒体内容和文件权限，点击“允许”
        if poco("com.android.permissioncontroller:id/permission_allow_button", text="始终允许").exists():
            poco("com.android.permissioncontroller:id/permission_allow_button", text="始终允许").click()
            time.sleep(3)
        else:
            pass

    else:
        print("用户非首次打开App！")
        time.sleep(15)
        pass

        # 判断插屏广告弹框是否存在，如果存在则关闭弹框
    if poco("bubei.tingshu:id/iv_advert_close").exists():
        # 点击关闭插屏广告
        poco("bubei.tingshu:id/iv_advert_close").click()
        time.sleep(3)
    else:
        print("插屏广告不存在！")
        time.sleep(3)
        pass

    # 判断青少年模式弹框是否存在，如果存在则关闭弹框
    if poco("bubei.tingshu:id/tv_close").exists():
        # 关闭青少年模式
        poco("bubei.tingshu:id/tv_close").click()
        time.sleep(3)
    else:
        print("青少年弹框不存在！")
        time.sleep(3)
        pass

    # 判断页脚悬浮广告是否存在，如果存在则关闭
    if poco("bubei.tingshu:id/closeIcon").exists():
        poco("bubei.tingshu:id/closeIcon").click()
    else:
        print("页脚悬浮广告不存在！")
        time.sleep(3)
        pass

    # 关闭APP首页弹的华为优惠弹框
    if poco("com.huawei.hwid:id/close_image").exists():
        poco("com.huawei.hwid:id/close_image").click()
    else:
        print("华为优惠弹框不存在！")
        time.sleep(3)
        pass