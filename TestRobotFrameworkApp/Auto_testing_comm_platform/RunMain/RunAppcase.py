s = '''
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +代码无bug
'''
print(s)
import unittest, os
from Auto_testing_comm_platform.Comm.HTMLTestRunner import *
from Auto_testing_comm_platform.Comm.SendMail import *

# 定义测试用例目录
Test_case_path =os.getcwd()+'\\Testcase'#getcwd当前目录
# 定义测试报告目录
Test_report_path = os.getcwd()+'\\Report'
Test_report_name = Test_report_path+"\\Appium_Auto_test_Report.html"
# 搜索测试用例
suit = unittest.defaultTestLoader.discover(Test_case_path,pattern='KaoyanApp_case.py')
# print(suit)
# 执行测试用例+写报告
f = open(Test_report_name,'wb') #创建文档并且以二进制写入
HTMLTestRunner(stream=f,title='考研app自动化测试报告').run(suit)
f.close()#关闭文档

# 发邮件
mail = SendMail()
mail.Add_text('考研app自动化测试报告',Subject,From,To)
mail.Add_file(Test_report_name,'Appium_Auto_test_Report.html')
mail.Send(server,port,MailUser,MailPwd,To_addr)
