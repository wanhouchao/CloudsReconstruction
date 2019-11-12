from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Appium import *
from appium import webdriver
from Auto_testing_comm_platform.Comm.Base import *

'''数据'''
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "P1QRMXEN4U",
    "appPackage": "com.example.administrator.websc",
    "appActivity": "com.app.ui.activity.LoginActivity",
    "unicodeKeyboard": "False",
    "resetKeyboard": "False",
    "noReset": "False",
}
url = 'http://logistics-admin-test.epsit.cn:6066/#/dashboard'  # 后台管理
user = 'admin'
psw = 'adminadmin'

import unittest  # 轻量级测试框架


class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        self.driver = APPIUM(desired_caps)
        # self.br = SeleniumFramework()
        print('开始')

    def tearDown(self) -> None:  # 还原测试环境
        self.driver.Out()
        print('结束')

    def LoginApp(self, RobotUser, RobotPassword):
        self.driver.Write('id=com.example.administrator.websc:id/et_login_account', RobotUser)
        self.driver.Write('id=com.example.administrator.websc:id/et_login_password', RobotPassword)
        self.driver.Click('id=com.example.administrator.websc:id/btn_login')
        time.sleep(10)
        print('等待登录10s后开始运行\n')

    def test_SpanFloor_001(self):  # 测试用例
        '''跨楼层优化'''
        # login
        RobotUser = 'test01'
        RobotPassword = '123456'
        self.driver.Write('id=com.example.administrator.websc:id/et_login_account', RobotUser)
        self.driver.Write('id=com.example.administrator.websc:id/et_login_password', RobotPassword)
        self.driver.Click('id=com.example.administrator.websc:id/btn_login')
        time.sleep(10)
        print('等待登录10s后开始运行\n')
        # 发送任务
        # self.driver.Click('xpath=//*[@text="配送"]')
        self.driver.Click('id=com.example.administrator.websc:id/rl_home_transport')
        self.driver.Click('id=com.example.administrator.websc:id/btn_pwd_btn21')
        self.driver.Click('id=com.example.administrator.websc:id/btn_pwd_btn22')
        self.driver.Click('id=com.example.administrator.websc:id/btn_pwd_btn23')
        self.driver.Click('id=com.example.administrator.websc:id/btn_pwd_btn24')
        self.driver.Click('xpath=//*[@text="位置A"]')
        self.driver.Click('xpath=//*[@text="实施"]')
        self.driver.Click('xpath=//*[@text="位置B"]')
        self.driver.Click('xpath=//*[@text="出发"]')

