from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Config.test_epsit import *
from time import sleep

import unittest  # 轻量级测试框架

# 数据
DataTable = DataTable('TimedCharging', 2)
TimeList = time.localtime(time.time())
Time = str(TimeList[3])+':'+str(TimeList[4]+2)

class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # Clear_environment()  # 清理web环境
        self.br = SeleniumFramework()
        self.br.Open_url(Robot_url)
        #登录
        self.br.Write('css=input[placeholder="用户名"]', 'admin')
        self.br.Write('css=input[placeholder="密码"]', 'adminadmin')
        self.br.Click('xpath=//button[contains(.,"登录")]')
        # 展开菜单
        self.br.Click('xpath=/html/body/div[1]/header/button[2]')
        self.br.Click('xpath=//li[contains(.," 系统管理")]')
        self.br.Click('css=a[href="#/sys/officeConfig"]')


    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def Login(self, DataTable, CaseId):
        '''登录函数'''
        self.br.Write('css=input[placeholder="用户名"]', DataTable['test_case' + str(CaseId)][1])
        self.br.Write('css=input[placeholder="密码"]', DataTable['test_case' + str(CaseId)][2])
        self.br.Click('xpath=//button[contains(.,"登录")]')
        # 展开菜单
        self.br.Click('xpath=/html/body/div[1]/header/button[2]')

    def Asser(self, DataTable, CaseId, string_ele):
        '''断言函数'''
        try:
            result = self.br.Text_up(string_ele)  # 提取结果
            print('实际结果：' + result)
        except:
            result = None
        print('预期结果：' + DataTable['test_case' + str(CaseId)][3])
        self.assertEqual(result, DataTable['test_case' + str(CaseId)][3], "对比结果不一致")  # 断言函数，对比两个是否一致


    def test_TimedCharging_001(self):
        # self.br.Click('css=button[title="增加"]')
        CaseId='1'
        self.br.Click('xpath=//span[text()="%s"]'%DataTable['test_case' + str(CaseId)][1])
        self.br.Click('css=a[title="修改"]')
        self.br.Write(DataTable['test_case' + str(CaseId)][2],Time)
        self.br.Click('xpath=//span[text()="提交"]')
        try:
            result = self.br.Text_up('css=div[class="ivu-loading-bar-inner ivu-loading-bar-inner-color-primary"][style="width: 0%; height: 2px;"]')  # 提取结果
        except:
            result = None
        print('实际结果：' + result)
        print('预期结果：' + DataTable['test_case' + str(CaseId)][3])
        self.assertEqual(result, '机构配置信息', "对比结果不一致")  # 断言函数，对比两个是否一致




if __name__ == "__main__":
    unittest.main()
