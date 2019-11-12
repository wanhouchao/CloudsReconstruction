from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Appium import *
from appium import webdriver
from Auto_testing_comm_platform.Comm.Base import *

'''数据'''
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "192.168.12.102:5555",
    "appPackage": "com.example.administrator.websc",
    "appActivity": "com.app.ui.activity.LoginActivity",
    "unicodeKeyboard": "True",
    "resetKeyboard": "True",
    "noReset": "True"
}
url = 'http://logistics-admin-test.epsit.cn:6066/#/dashboard'  # 后台管理
user = 'admin'
psw = 'adminadmin'

import unittest  # 轻量级测试框架


class Robot_system(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = APPIUM(desired_caps)
        self.driver.Click('id=com.example.administrator.websc:id/btn_login')
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.Click('xpath=//*[@text="取消任务"]')
        self.driver.Click('xpath=//*[@text="1"]')
        self.driver.Click('xpath=//*[@text="2"]')
        self.driver.Click('xpath=//*[@text="3"]')
        self.driver.Click('xpath=//*[@text="4"]')
        self.driver.Out()


    def test_001(self):
        '''单任务崩溃'''
        self.driver.Click('id=com.example.administrator.websc:id/rl_home_transport')
        self.driver.Click('xpath=//*[@text="1"]')
        self.driver.Click('xpath=//*[@text="2"]')
        self.driver.Click('xpath=//*[@text="3"]')
        self.driver.Click('xpath=//*[@text="4"]')
        self.driver.Click('xpath=//*[@text="茶水间"]')
        self.driver.Click('xpath=//*[@text="出发"]')
        self.driver.Click('xpath=//*[@text="崩溃"]')
        time.sleep(20)
        try:
            result = self.driver.Text_up('xpath=//*[@text="茶水间"]')
        except:
            result = '没有'

        self.assertEqual(result, '茶水间', '对比结果不一致')

    def test_002(self):
        '''多任务崩溃'''
        self.driver.Click('id=com.example.administrator.websc:id/rl_home_transport')
        self.driver.Click('xpath=//*[@text="1"]')
        self.driver.Click('xpath=//*[@text="2"]')
        self.driver.Click('xpath=//*[@text="3"]')
        self.driver.Click('xpath=//*[@text="4"]')
        self.driver.Click('xpath=//*[@text="茶水间"]')
        self.driver.Click('xpath=//*[@text="实施"]')
        self.driver.Click('xpath=//*[@text="出发"]')
        self.driver.Click('xpath=//*[@text="崩溃"]')
        time.sleep(20)
        try:
            result = self.driver.Text_up('xpath=//*[@text="茶水间"]')
        except:
            result = '没有'
        self.assertEqual(result, '茶水间', '对比结果不一致')


if __name__ == "__main__":
    unittest.main()
