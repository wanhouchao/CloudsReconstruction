import unittest
from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from ddt import ddt, unpack, data

DataPath = u'E:\PyCharm\location\Auto_testing_comm_platform\Testcase\LogisticsAdminTest\EpsBackData.xls'

DataLowPower = Excel(DataPath).DataUp(u'低电量充电')['data']
DataFreePower = Excel(DataPath).DataUp(u'闲时充电')['data']


@ddt
class Robot_system(unittest.TestCase):
    # @classmethod
    # def setUpClass(self) -> None:
    #     self.br= SeleniumFramework()

    def setUp(self) -> None:  # 前置条件
        self.br = SeleniumFramework()
        self.br.Open_url(Robot_url)
        # 登录
        self.br.Write('css=input[placeholder="用户名"]', 'admin')
        self.br.Write('css=input[placeholder="密码"]', 'adminadmin')
        self.br.Click('xpath=//button[contains(.,"登录")]')
        # 展开菜单
        self.br.Click('xpath=/html/body/div[1]/header/button[2]')
        self.br.Click('xpath=//li[contains(.," 系统管理")]')
        self.br.Click('css=a[href="#/sys/officeConfig"]')

    # @classmethod
    # def tearDownClass(self) -> None:
    #     self.br.Out()
    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    @data(*DataLowPower)
    def test_LowPower_001(self, Data):
        '''机构配置设置低电量99%'''
        print('测试标题：' + Data[0])
        OrganizationName = Data[1]  # 机构名称从excel里面读取
        Power = Data[2]
        Mode = Data[3]
        ExpectedResult = Data[4]
        print('预期结果：' + ExpectedResult)
        self.br.Click('xpath=//span[contains(.,"%s")]' % OrganizationName)
        self.br.Click('css=a[href="javascript:"]')
        self.br.Write('css=input[placeholder="输入电量低去充电设置（默认30%）"]', Power)
        self.br.Click('xpath=//label[contains(.,"运行模式")]/../div/div')
        self.br.Click('xpath=//li[contains(.,"%s")]' % Mode)
        self.br.Click('xpath=//span[contains(.,"提交" )]')
        try:
            ActualResult = self.br.Text_up('xpath=/html/body/div[1]/div/main/div/div/div[1]/div[1]/div/div[1]/div')
        except:
            ActualResult = ''
        print('实际结果：' + ActualResult)
        self.assertEqual(ActualResult, ExpectedResult, '对比结果不一致')

    @data(*DataFreePower)
    def test_LowPower_002(self, Data):
        '''机构配置设置低电量99%'''
        print('测试标题：' + Data[0])
        OrganizationName = Data[1]  # 机构名称从excel里面读取
        Power = Data[2]
        Time = Data[3]
        Mode = Data[4]
        ExpectedResult = Data[5]
        print('预期结果：' + ExpectedResult)
        self.br.Click('xpath=//span[contains(.,"%s")]' % OrganizationName)
        self.br.Click('css=a[href="javascript:"]')
        self.br.Write('css=input[placeholder="输入闲时充电时间（秒）"]', Time)
        self.br.Write('css=input[placeholder="输入闲时充电电量（%）"]', Power)
        self.br.Click('xpath=//label[contains(.,"运行模式")]/../div/div')
        self.br.Click('xpath=//li[contains(.,"%s")]' % Mode)
        self.br.Click('xpath=//span[contains(.,"提交" )]')
        try:
            ActualResult = self.br.Text_up('xpath=/html/body/div[1]/div/main/div/div/div[1]/div[1]/div/div[1]/div')
        except:
            ActualResult = ''
        print('实际结果：' + ActualResult)
        self.assertEqual(ActualResult, ExpectedResult, '对比结果不一致')


if __name__ == "__main__":
    unittest.main()
