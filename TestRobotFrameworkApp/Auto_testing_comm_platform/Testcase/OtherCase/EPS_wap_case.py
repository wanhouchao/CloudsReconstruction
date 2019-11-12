from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Config.test_epsit import *
from time import sleep

import unittest  # 轻量级测试框架

# 数据
DataTable = DataTable('手机wap')
url = 'http://logistics-api-test.epsit.cn:6066/m/#/login'


class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # Clear_environment()  # 清理web环境
        self.br = SeleniumFramework('wap', 'ge')
        self.br.Open_url(url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def Login(self, DataTable, CaseId):
        print('测试标题：' + DataTable['test_case' + str(CaseId)][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case' + str(CaseId)][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case' + str(CaseId)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')

    def Asser(self, DataTable, CaseId, result):
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"%s")]' % str(result))  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        print('预期结果：' + DataTable['test_case' + str(CaseId)][3])
        self.assertEqual(result, DataTable['test_case' + str(CaseId)][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_test(self):
        CaseId = '7'
        result = '立即呼叫'
        self.Login(DataTable, CaseId)
        self.Asser(DataTable, CaseId, result)

    def test_login_001(self):  # 测试用例
        '''输入正确的用户名'''
        print('测试标题：' + DataTable['test_case1'][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case1'][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case1'][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"立即呼叫")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case1'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_002(self):  # 测试用例
        i = '2'
        print('测试标题：' + DataTable['test_case' + str(i)][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case' + str(i)][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case' + str(i)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"机器人用户不存在")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case' + str(i)][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_003(self):  # 测试用例
        i = '3'
        print('测试标题：' + DataTable['test_case' + str(i)][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case' + str(i)][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case' + str(i)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"密码错误")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case' + str(i)][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_004(self):  # 测试用例
        i = '4'
        print('测试标题：' + DataTable['test_case' + str(i)][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case' + str(i)][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case' + str(i)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"密码不能为空！")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case' + str(i)][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_005(self):  # 测试用例
        print('测试标题：' + DataTable['test_case5'][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case5'][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case5'][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"账号不能为空！")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case5'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_006(self):  # 测试用例
        i = '6'
        print('测试标题：' + DataTable['test_case' + str(i)][0])
        self.br.Write('css=input[placeholder="Your name"]', DataTable['test_case' + str(i)][1])
        self.br.Write('css=input[type="password"]', DataTable['test_case' + str(i)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"密码不能为空！")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case' + str(i)][3], "对比结果不一致")  # 断言函数，对比两个是否一致


if __name__ == "__main__":
    unittest.main()
