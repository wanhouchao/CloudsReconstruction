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
　　　　　┃　　　┃
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
from Auto_testing_comm_platform.Comm.HTMLTestRunner import *
from Auto_testing_comm_platform.Comm.SendMail import *
from Auto_testing_comm_platform.Testcase.LogisticsAdminTest.LowPowerChargeCase import *

# 定义测试用例目录
Test_case_path =os.getcwd()[:-8]+'\\Testcase\\LogisticsAdminTest'#getcwd当前目录
# 定义测试报告目录
Test_report_path = os.getcwd()[:-8]+'\\Report'
Test_report_name = Test_report_path+"\\LogisticsAdminTest_RobotTestReport.html"
# 搜索测试用例
suit = unittest.defaultTestLoader.discover(Test_case_path,pattern='LowPowerChargeCase.py')
# suit1 = unittest.defaultTestLoader.discover(Test_case_path,pattern='LowPowerChargeCase.py')
# 执行测试用例+写报告
f = open(Test_report_name,'wb') #创建文档并且以二进制写入
HTMLTestRunner(stream=f,title='自动化测试报告').run(suit)
# HTMLTestRunner(stream=f,title='自动化测试报告').run(suit1)
f.close()#关闭文档

# 发邮件
mail = SendMail()
mail.Add_text('自动化测试报告',Subject,From,To)
mail.Add_file(Test_report_name,'LogisticsAdminTest_RobotTestReport.html')
mail.Send(server,port,MailUser,MailPwd,To_addr)


