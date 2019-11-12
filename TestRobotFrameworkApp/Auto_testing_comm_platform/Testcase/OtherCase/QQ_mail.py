from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Comm.Base import *
from Auto_testing_comm_platform.Config.TestEnv import *

import unittest  # 轻量级测试框架


class Ranzhi(unittest.TestCase):
    def setUp(self) -> None:  # 前置条件
        Clear_environment()#清理web环境
        self.br = SeleniumFramework('ge')
        self.br.Open_url(QQ_url)

    def tearDown(self) -> None:  # 还原测试环境
        self.br.Out()

    def test_login_001(self):  # 测试用例
        '''这里写测试用例标题  测试输入正确的用户名密码登录'''
        # 操作步骤
        self.br.Switch_to('login_frame')
        self.br.Write('id=u',User)
        self.br.Write('id=p',password)
        self.br.Click('id=login_button')
        self.br.Default_content()
        time.sleep(2)
        #self.br.Switch_to('actionFrame')
        try:
            result =self.br.Text_up('css=span[title="关联其他QQ邮箱"]')#提取结果
            print(result)
        except:
            result=''
        self.assertEqual(result,'1154887004@qq.com',"对比结果不一致")#断言函数，对比两个是否一致
    #
    # def test_login_002(self):
    #     '''测试发邮件的功能'''
    #     self.br.Switch_to('login_frame')
    #     self.br.Write('id=u', User)
    #     self.br.Write('id=p', password)
    #     self.br.Click('id=login_button')
    #     #self.br.Click('id=login_button')
    #     self.br.Click('id=composebtn')
    #     #time.sleep(2)
    #     self.br.Switch_to('mainFrame')

if __name__=='__main__':
    unittest.main()