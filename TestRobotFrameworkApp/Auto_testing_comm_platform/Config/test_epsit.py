import os
from Auto_testing_comm_platform.Comm.DateDriver import *
#登录
User = 'admin'
password = 'admin'
#后台管理
Robot_url = 'http://logistics-admin-test.epsit.cn:6066/#/auth/login?redirect=%2Fdashboard'#测试环境

#添加用户
Institutions = '图片测试'
RobotUserName='test009'
RobotUserPassword='1234'
RobotUserNickname='QWER'

if __name__=='__main__':
    from Auto_testing_comm_platform.Comm.SeleniumFramework import *
    from Auto_testing_comm_platform.Comm.Appium import *
    from Auto_testing_comm_platform.Comm.Base import *
    # #后台查询
    br = SeleniumFramework()
    br.Open_url('http://logistics-admin-test.epsit.cn:6066/#/auth/login?redirect=%2Fdashboard')
    #     #login
    br.Write('css=input[placeholder="用户名"]', 'admin')
    br.Write('css=input[placeholder="密码"]', 'adminadmin')
    br.Click('css=button[class="btn btn-primary px-4"]')
    #     #展开菜单-->机器人管理-->位置管理
    br.Click('css=button[class="navbar-toggler sidebar-toggler d-md-down-none"]')
    br.Click('xpath=//li[contains(.," 机器人管理")]')
    br.Click('css=a[href="#/device/robotPosition"]')
    #     #点击机构
    # br.Click('xpath=//li[contains(.,u"MIR医院D")]')
    #     #获取时间
    result = br.Text_up(
        'xpath=/html/body/div[1]/div/main/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/span')
    print(TimeTranslate(result))
    br.Out()
