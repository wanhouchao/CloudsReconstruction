from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *
from Auto_testing_comm_platform.Config.test_epsit import *
from time import sleep
from ddt import ddt, data, unpack
import unittest  # 轻量级测试框架
from Auto_testing_comm_platform.Comm.DateDriver import *

# 数据r
DataTable = Excel(r'E:\PyCharm\location\Auto_testing_comm_platform\Data\login.xlsx')
Data = DataTable.ReadRowsTable('login')
Title = Data
@ddt
class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # Clear_environment()  # 清理web环境
        print(Data)
        self.br = SeleniumFramework()
        self.br.Open_url(Robot_url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    @data(*Data)
    def test_login_001(self,value):  # 测试用例
        print(value[1],value[2])

if __name__ == '__main__':
    unittest.main()