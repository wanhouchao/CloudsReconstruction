from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Config.test_epsit import *
from time import sleep

import unittest  # 轻量级测试框架

# 数据
DataTable = DataTable('login',2)
# SheetName = 'login'
# case_data_path = os.getcwd()[:-8] + 'Data\login.xlsx'
# print(case_data_path)
# data = ReadExcel(case_data_path)
# DataTable = data.Getdata('name=' + SheetName)

class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # Clear_environment()  # 清理web环境
        self.br = SeleniumFramework()
        self.br.Open_url(Robot_url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def test_login_001(self):  # 测试用例
        '''输入正确的用户名'''
        print('测试标题：' + DataTable['test_case1'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case1'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case1'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//a[contains(.,"易普森医院物流机器人管理系统")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case1'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_002(self):  # 测试用例
        '''输入错误的用户名'''
        print('测试标题：' + DataTable['test_case2'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case2'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case2'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//p[contains(.,"登入你的账户")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case2'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_003(self):  # 测试用例
        '''输入错误的密码'''
        print('测试标题：' + DataTable['test_case3'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case3'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case3'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//p[contains(.,"登入你的账户")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case3'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_004(self):  # 测试用例
        '''用户名密码都不输入'''
        print('测试标题：' + DataTable['test_case4'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case4'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case4'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//p[contains(.,"登入你的账户")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case4'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_005(self):  # 测试用例
        '''不输入用户名'''
        print('测试标题：' + DataTable['test_case5'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case5'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case5'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//p[contains(.,"登入你的账户")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case5'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_006(self):  # 测试用例
        '''不输入密码'''
        print('测试标题：' + DataTable['test_case6'][0])
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case6'][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case6'][2])
        self.br.Click('css=button[class="btn btn-primary px-4"]')
        try:
            result = self.br.Text_up('xpath=//p[contains(.,"登入你的账户")]')  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        self.assertEqual(result, DataTable['test_case6'][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def Login(self, DataTable, CaseId):
        '''登录函数'''
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case' + str(CaseId)][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case' + str(CaseId)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        # 展开菜单
        self.br.Click('xpath=//button[contains(.,"☰")]')

    def Asser(self, DataTable, CaseId, result):
        '''断言函数'''
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"%s")]' % str(result))  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        print('预期结果：' + DataTable['test_case' + str(CaseId)][3])
        self.assertEqual(result, DataTable['test_case' + str(CaseId)][3], "对比结果不一致")  # 断言函数，对比两个是否一致


if __name__=="__main__":
    # E:\PyCharm\location\Auto_testing_comm_platform\Testcase\LogisticsAdminTest
    unittest.main()