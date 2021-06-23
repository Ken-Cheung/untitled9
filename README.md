### 框架目前需要修改： <br>
<该任务已经完成><br>
~~installAPK.py文件需要修改安装逻辑,4个pro安装pro安装包，其余的安装非Pro安装包~~ <br>
```python
# 区分pro和非Pro的思路：
# Pro和非pro是通过package名字区分，bubei.tingshu bubei.tingshu.pro
# 除了ov小米魅族，其他两个就是非pro，除了华为，其余都安装App Store版本
```
<该任务已经完成><br>
~~对测试用例输出测试报告（测试报告需要带截图）~~ <br>
```python
# 通过该方法可以将截图附注到allure页面上，还有一种方法是断言失败后自动截图   
with open('./screencap/122222222.png',mode='rb') as f:
        file = f.read()
        allure.attach(file, '未登录', allure.attachment_type.PNG)
```
<该任务已经完成><br>
~~多个设备就输出多个测试报告，在根目录下的report目录中~~<br>
```python
# 在report目录之中，通过当前机型的name生成本次运行的测试用例
--alluredir=./report/{deviceName}
```

---
### 已知问题：<br>
1. ADB设备断线，该问题与自动化脚本并没什么关系，重新连接上手机又可以执行了


### 测试用例方面
首页用例<br>
下载<br>
播放器<br>
覆盖升级<br>