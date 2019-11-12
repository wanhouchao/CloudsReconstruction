from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Comm.Appium import *

import unittest  # 轻量级测试框架

class kaoyam(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        '''手动adb连接手机打开appium，连接上app'''
        self.der = APPIUM(kaoyan_desired_caps)

    def tearDown(self) -> None:  # 还原测试环境
        '''退出app'''
        self.der.Out()

