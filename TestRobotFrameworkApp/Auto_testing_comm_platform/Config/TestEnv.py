
#腾讯qq
QQ_url = 'https://mail.qq.com/'
User = '1154887004'
password = 'LIYULU1314520'


# 邮箱信息
server = 'smtp.qq.com'  # 填写qq邮箱smtp地址
port = 465  # 端口
MailUser = '1154887004@qq.com'  # 邮箱账号
MailPwd = 'uwghwjaqyksgjidh'  # 邮箱授权码 qq、新浪是授权码登录  网易是密码登录
To_addr = '1154887004@qq.com'  # 收件人邮箱地址
Text = '自动化测试报告' # 邮件正文内容
Subject = '自动化测试报告'  # 邮件主题
From = '万厚超'  # 发件人
To = '万厚超'  # 收件人

# Mysql数据
Mysqluser = 'root'
Mysqlpwd = '123456'
Mysqlserver = '192.168.1.6'
Mysqldatabase = 'info'
#Mysql(epsfrontserver)
epsfrontserverUser = 'epsit'
epsfrontserverPwd = 'epsit'
epsfrontserverServer = '192.168.3.66'
epsfrontserverDatabase = 'epsfrontserver'
#app信息
qq_desired_caps ={
  "platformName": "Android",#app安装的系统
  "platformVersion": "5.1.1",#系统版本
  "deviceName": "127.0.0.1:21503",#连接手机的名字在cmd 用adb devices -l查询
    'app':r'F:\qqlite_3.7.1.704_android_r110206_GuanWang_537057973_release_10000484.apk',#app在win上的位置
  "appPackage": "com.tencent.qqlite",#app在手机里面的名字
#app的Activity 用aapt dump badging xxx.apk | find "launchable-activity"查找
  "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
  "noReset": True
}
kaoyan_desired_caps ={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:21503",
    # 'app':r'C:\Users\dell\Desktop\kaoyanbang_3.4.1.251.apk',
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}
eps_desired_caps ={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "192.168.12.101:5006", #"192.168.12.102:5555"
    # 'app':r'C:\Users\dell\Desktop\kaoyanbang_3.4.1.251.apk',
  "appPackage": "com.eps.logistics.yone",
  "appActivity": "com.app.ui.activity.LoginActivity",
  # "noReset": True
} 
#
Robot_user = 'admin'
Robot_password = 'adminadmin'
#文件夹path
Autopath =  'E:\PyCharm\location\Auto_testing_comm_platform'