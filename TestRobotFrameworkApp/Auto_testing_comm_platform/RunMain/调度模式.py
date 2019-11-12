import os, time
from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Config.test_epsit import *

# 登录
br = SeleniumFramework('ge')
br.Open_url(Robot_url)
br.Write('css=input[placeholder="用户名"]', Robot_user)
br.Write('css=input[placeholder="密码"]', Robot_password)
br.Click('css=button[class="btn btn-primary px-4"]')
# 点击首页
br.Click('css=a[href="#/"]')
# 点击菜单
br.Click('css=button[class="navbar-toggler sidebar-toggler d-md-down-none"]')
# 进入系统管理--》机构配置管理
br.Click('xpath=//li[contains(.," 系统管理")]')
br.Click('css=a[href="#/sys/officeConfig"]')
# 选择云迹Y1医院D1
br.Click('xpath=//span[contains(.,"云迹Y1医院D1")]')
# 点击修改
br.Click('css=[class="fa fa-pencil-square-o text-primary"]')
# 找到运行模式
br.Click('xpath=//label[contains(.,"运行模式")]/../div/div')
br.Click('xpath=//label[contains(.,"运行模式")]/../div/div/div[2]/ul[2]/li[2]')
time.sleep(0.5)
# 配置安全距离和危险距离
br.Write('css=input[placeholder="输入安全距离 "]', '4')
br.Write('css=input[placeholder="输入危险距离"]', '3')
time.sleep(0.5)
# 点击提交
br.Click('css=button[class="ivu-btn ivu-btn-info"]')
time.sleep(0.5)
#收菜单点击系统管理
br.Click('xpath=//li[contains(.," 系统管理")]')
time.sleep(0.5)
#点击调度管理-->管制等待区域
br.Click('xpath=//li[contains(.," 调度管理")]')
br.Click('css=a[href="#/schedule/controlTrafficAreaController"]')
time.sleep(0.5)
# 选择云迹Y1医院D1
br.Click('xpath=//span[contains(.,"云迹Y1医院D1")]')
time.sleep(0.5)
#管制等待区域管理
br.Click('css=a[title="管制等待区域管理"]')
br.Click('css=button[title="增加"]')
br.Write('css=input[placeholder="输入备注"]','自动化测试')
time.sleep(0.5)
# 点击提交
br.Click('css=button[class="ivu-btn ivu-btn-info"]')
time.sleep(0.5)
#配置点位
br.Click('xpath=//td[contains(.,"自动化测试")]/../td[4]/a[1]')
time.sleep(0.5)
#添加点
br.Click('css=button[title="增加"]')
br.Click('xpath=//label[contains(.,"管制等待区域位置名称")]/../div/div')
br.Click('xpath=//li[contains(.,"停靠点10_1_走廊3停靠点1")]')
br.Click('xpath=//i[contains(.,"提交")]')
time.sleep(5)
br.Out()
