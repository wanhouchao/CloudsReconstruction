from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Appium import *
from appium import webdriver
import unittest  # 轻量级测试框架
from Auto_testing_comm_platform.Comm.Base import *
'''数据'''
desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "P1QRME5O58",
        "appPackage": "com.example.administrator.websc",
        "appActivity": "com.app.ui.activity.LoginActivity",
        "unicodeKeyboard": "True",
        "resetKeyboard": "True",
        "noReset": "False"
    }
url = 'http://logistics-admin-test.epsit.cn:6066/#/dashboard'#后台管理
user ='admin'
psw = 'adminadmin'

class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        print('开始')

    def tearDown(self) -> None:  # 还原测试环境
        print('结束')


