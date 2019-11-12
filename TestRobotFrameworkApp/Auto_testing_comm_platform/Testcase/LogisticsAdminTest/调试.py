
import unittest
from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from ddt import ddt, unpack, data
#
DataPath = u'E:\PyCharm\location\Auto_testing_comm_platform\Testcase\LogisticsAdminTest\EpsBackData.xls'
Data = Excel(DataPath).DataUp(u'调试')['data'][0]
OrganizationName = Data[0] # 机构名称从excel里面读取
Power =Data[1]
Mode =Data[3]

br = SeleniumFramework()
br.Open_url(Robot_url)

# 登录
br.Write('css=input[placeholder="用户名"]', 'admin')
br.Write('css=input[placeholder="密码"]', 'adminadmin')
br.Click('xpath=//button[contains(.,"登录")]')
# 展开菜单
br.Click('xpath=/html/body/div[1]/header/button[2]')
br.Click('xpath=//li[contains(.," 系统管理")]')
br.Click('css=a[href="#/sys/officeConfig"]')

br.Click('xpath=//span[contains(.,"%s")]' % OrganizationName)
br.Click('css=a[href="javascript:"]')
br.Write('xpath=/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[7]/div/div/input','')
br.Write('xpath=/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[8]/div/div/input', '60')
# time.sleep(5)
# br.Click('xpath=//label[contains(.,"运行模式")]/../div/div')
# br.Click('xpath=//li[contains(.,"%s")]' % Mode)
# br.Click('xpath=//span[contains(.,"提交" )]')
br.Click('xpath=/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[25]/div/button[1]')



