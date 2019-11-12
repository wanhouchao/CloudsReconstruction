from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Comm.Appium import *

import unittest  # 轻量级测试框架

# 数据
DataTable = DataTable('login')
url = 'http://logistics-admin-test.epsit.cn:6066/#/auth/login?redirect=%2Fdashboard'


class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # Clear_environment()  # 清理web环境
        self.br = SeleniumFramework()
        self.br.Open_url(url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def Login(self, DataTable, CaseId):
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case' + str(CaseId)][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case' + str(CaseId)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        #展开菜单
        self.br.Click('xpath=//button[contains(.,"☰")]')



    def Asser(self, DataTable, CaseId, result):
        try:
            result = self.br.Text_up('xpath=//span[contains(.,"%s")]' % str(result))  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        print('预期结果：' + DataTable['test_case' + str(CaseId)][3])
        self.assertEqual(result, DataTable['test_case' + str(CaseId)][3], "对比结果不一致")  # 断言函数，对比两个是否一致

    def test_login_test(self):
        CaseId = '1'
        # print('测试标题：' + DataTable['test_case' + str(CaseId)][0])
        self.Login(DataTable, CaseId)
        time.sleep(10)




if __name__ == "__main__":
    unittest.main()
