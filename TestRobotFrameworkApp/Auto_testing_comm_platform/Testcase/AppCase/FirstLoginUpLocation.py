from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Appium import *
from appium import webdriver
from Auto_testing_comm_platform.Comm.Base import *
'''数据'''
desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "P1QRME5O58",
        "appPackage": "com.example.administrator.websc",
        "appActivity": "com.app.ui.activity.LoginActivity",
        "unicodeKeyboard": "True",
        "resetKeyboard": "True",
        "noReset": "False"
    }
url = 'http://logistics-admin-test.epsit.cn:6066/#/dashboard'#后台管理
user ='admin'
psw = 'adminadmin'

import unittest  # 轻量级测试框架


class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        # self.driver = APPIUM(desired_caps)
        # self.br = SeleniumFramework()
        print('开始')

    def tearDown(self) -> None: # 还原测试环境
        # self.br.Out()
        print('结束')

    def LoginApp(self,user,password):
        self.driver=APPIUM(desired_caps)
        self.driver.Write('id=com.example.administrator.websc:id/et_login_account',user)
        self.driver.Write('id=com.example.administrator.websc:id/et_login_password',password)
        self.driver.Click('id=com.example.administrator.websc:id/btn_login')

    def test_login_001(self):  # 测试用例
        '''第一次登录上传位置'''
        # login
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.find_element_by_id("com.example.administrator.websc:id/et_login_account").send_keys("robot01")
        driver.find_element_by_id("com.example.administrator.websc:id/et_login_password").send_keys("123456")
        driver.find_element_by_id("com.example.administrator.websc:id/btn_login").click()
        ExpectedResult = time.time()#获取当前时间戳
        # #后台查询
        br = SeleniumFramework()
        br.Open_url(url)
        #     #login
        br.Write('css=input[placeholder="用户名"]', user)
        br.Write('css=input[placeholder="密码"]', psw)
        br.Click('css=button[class="btn btn-primary px-4"]')
        #     #展开菜单-->机器人管理-->位置管理
        br.Click('css=button[class="navbar-toggler sidebar-toggler d-md-down-none"]')
        br.Click('xpath=//li[contains(.," 机器人管理")]')
        br.Click('css=a[href="#/device/robotPosition"]')
        #     #点击机构
        # br.Click('xpath=//li[contains(.,u"MIR医院D")]')
        #     #获取时间
        ActualResult = br.Text_up('xpath=/html/body/div[1]/div/main/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/span')
        print(ActualResult)
        if int(TimeTranslate(ActualResult))-int(ExpectedResult)<30:
            self.assertEqual(1, 1, '对比结果不一致')
        else:
            self.assertEqual(1, 2, '对比结果不一致')

if __name__ == "__main__":
    unittest.main()
