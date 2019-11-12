from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from time import sleep

import unittest  # 轻量级测试框架


class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        #Clear_environment()  # 清理web环境
        self.br = SeleniumFramework('ge')
        self.br.Open_url(Robot_url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def test_login_001(self):  # 测试用例
        '''这里写测试用例标题  测试输入正确的用户名密码登录'''
        # 登录
