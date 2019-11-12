from Auto_testing_comm_platform.Comm.Appium import *
from ddt import ddt, unpack, data
import unittest  # 轻量级测试框架
from Auto_testing_comm_platform.Comm.Base import *

desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:21503",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "unicodeKeyboard": "True",  # 使用unicode输入法
    "resetKeyboard": "True",  # 重置输入法到初始状态
    "noReset": "False"  # 启动app时不要清除app里的原有的数据
}

DataPath = u'E:\PyCharm\location\Auto_testing_comm_platform\Data\login.xlsx'
DataLogin = Excel(DataPath).DataUp(u'考研')['data']


# print(DataLogin)

@ddt
class Robot_system(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        self.driver = APPIUM()
        self.driver.OpenApp(desired_caps)
        # pass

    def tearDown(self) -> None:  # 还原测试环境
        self.driver.Out()
        # pass

    @data(*DataLogin)
    def test_Login_001(self, Data):
        '''登录测试'''
        print('测试标题：' + Data[0])
        user = Data[1]
        pawd = Data[2]
        ExpectedResult = Data[3]
        print('预期结果：' + ExpectedResult)
        self.driver.TapClick(650, 39)
        self.driver.Write('id=com.tal.kaoyan:id/login_email_edittext', user)
        self.driver.Write('id=com.tal.kaoyan:id/login_password_edittext', pawd)
        self.driver.Click('id=com.tal.kaoyan:id/login_login_btn')
        try:
            ActualResult = self.driver.Text_up('id=com.tal.kaoyan:id/login_login_btn')
        except:
            ActualResult = ''
        print('实际结果：'+ActualResult)
        self.assertEqual(ActualResult, ExpectedResult, '对比结果不一致')


if __name__ == "__main__":
    unittest.main()
