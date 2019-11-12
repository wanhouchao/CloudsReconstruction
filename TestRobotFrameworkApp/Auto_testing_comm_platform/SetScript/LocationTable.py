from Auto_testing_comm_platform.Comm.SeleniumFramework import *

br = SeleniumFramework(br_name='ge')
br.Open_url('http://logistics-admin-test.epsit.cn:6066/#/auth/login')
# 登录
br.Write('css=input[placeholder="用户名"]', 'admin')
br.Write('css=input[placeholder="密码"]', 'adminadmin')
br.Click('xpath=//button[contains(.,"登录")]')
# 展开菜单
br.Click('xpath=/html/body/div[1]/header/button[2]')
br.Click('xpath=//li[contains(.," 调度管理")]')
br.Click('css=a[href="#/schedule/robotPositionMapping"]')
# 添加配置

for i in range(2, 3):
    br.Click('css=button[class="ivu-btn ivu-btn-success"][title="增加"]')
    br.Click('xpath=//label[text()="所属机构"]/../div/div/div/span')
    br.Click('xpath=//label[text()="所属机构"]/../div/div/div[2]/ul[2]/li[5]')
    time.sleep(0.5)

    br.Click('xpath=//label[text()="选择机器人类型(默认为MIR)"]/../div/div')
    br.Click('xpath=//label[text()="选择机器人类型(默认为MIR)"]/../div/div/div[2]/ul[2]/li[2]')  # Y1(云际)
    time.sleep(0.5)

    br.Click('xpath=//label[text()="机器人任务位置"]/../div/div')
    br.Click('xpath=//label[text()="机器人任务位置"]/../div/div/div[2]/ul[2]/li[%s]' % i)  # 1楼保安亭
    time.sleep(0.5)

    br.Click('xpath=//label[text()="映射的机器人类型(默认为云际)"]/../div/div')
    br.Click('xpath=//label[text()="映射的机器人类型(默认为云际)"]/../div/div/div[2]/ul[2]/li[3]')  # Y2(云际)
    time.sleep(0.5)

    br.Click('xpath=//label[text()="映射的机器人任务位置"]/../div/div')
    br.Click('xpath=//label[text()="映射的机器人任务位置"]/../div/div/div[2]/ul[2]/li[%s]' % i)  # 1楼保安亭
    time.sleep(0.5)

    status = br.Text_up('xpath=//label[text()="映射的机器人任务位置"]/../div/div/div[2]/ul[2]/li[%s]' % i)
    print(status)
    br.Click('xpath=//span[text()="提交"]')
    time.sleep(5)

br.Out()
