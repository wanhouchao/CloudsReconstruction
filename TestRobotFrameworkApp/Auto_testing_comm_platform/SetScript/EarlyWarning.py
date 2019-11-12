import time

from Auto_testing_comm_platform.Comm.SeleniumFramework import *


br = SeleniumFramework(br_name='ge')
br.Open_url('http://logistics-admin-test.epsit.cn:6066/#/auth/login')
# 登录
br.Write('css=input[placeholder="用户名"]', 'admin')
br.Write('css=input[placeholder="密码"]', 'adminadmin')
br.Click('xpath=//button[contains(.,"登录")]')
# 展开菜单
br.Click('xpath=/html/body/div[1]/header/button[2]')
br.Click('xpath=//li[contains(.," 运行监控管理")]')
br.Click('css=a[href="#/run/monitorStatus"]')
# 添加配置

for i in range(1, 28):
    br.Click('css=button[class="ivu-btn ivu-btn-success"][title="增加"]')
    br.Click('xpath=//label[text()="所属机构"]/../div/div/div/span')
    br.Click('xpath=//label[text()="所属机构"]/../div/div/div[2]/ul[2]/li[14]')
    time.sleep(0.5)
    br.Click('xpath=//span[contains(.,"输入机器人状态")]')
    status = br.Text_up('xpath=//label[text()="机器人状态"]/../div/div/div[2]/ul[2]/li[%s]'%i)
    br.Click('xpath=//label[text()="机器人状态"]/../div/div/div[2]/ul[2]/li[%s]'%i)
    print(status)
    br.Write('css=input[placeholder="输入异常状态时间间隔"]', '60')
    br.Write('css=input[placeholder="输入异常推送次数"]', '1')
    br.Click('xpath=//span[text()="选择预警级别"]')
    br.Click('xpath=//li[text()="高"]')
    time.sleep(0.5)
    br.Write('css=textarea[placeholder="输入备注信息"]', '机器人:'+status+'---60s')
    br.Click('xpath=//span[text()="提交"]')
    time.sleep(5)
br.Out()


# #配送预警信息
# br.Click('css=a[href="#/run/noticeConfig"]')
# br.Click('css=button[class="ivu-btn ivu-btn-success"][title="增加"]')
# br.Click('xpath=//label[text()="所属机构"]/../div/div/div/span[1]')
# br.Click('xpath=//label[text()="所属机构"]/../div/div/div[2]/ul[2]/li[14]')
# time.sleep(0.5)
# br.Click('xpath=//span[text()="选择预警类型"]')
# br.Click('xpath=//li[text()="不通知"]')
# time.sleep(0.5)
# br.Click('xpath=//span[text()="选择预警级别"]')
# br.Click('xpath=//li[text()="高"]')
# time.sleep(0.5)
# br.Click('xpath=//label[text()="联系人"]/../div/div/input')
