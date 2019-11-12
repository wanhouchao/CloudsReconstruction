import smtplib  # 连接邮箱服务器
from email.mime.multipart import MIMEMultipart  # 构造邮件正文和附件
from email.mime.text import MIMEText  # 构造邮件正文
import os, time
from Auto_testing_comm_platform.Config.TestEnv import *


class SendMail():
    def Add_text(self, Text, Subject, From, To):
        '''构建邮件文本和邮件主题'''
        self.mail = MIMEMultipart()
        # 构建邮件正文 第一个参数内容 第二个参数格式() 第三个编码方式
        text = MIMEText(Text, 'plain', 'utf-8')
        self.mail.attach(text)  # 添加正文
        # 构建邮件主题
        self.mail['Subject'] = Subject
        self.mail['From'] = From
        self.mail['To'] = To

    def Add_file(self, file, filename):
        '''
        file=附件在电脑里面的地址和名字 如：F:\\temp.html
        filename  = 附件名字  如： temp.html必须是.html后缀
        '''
        file = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
        file["Content-Type"] = 'application/octet-stream'  # 内容的类型  邮件附件的类型
        file["Content-Disposition"] = 'attachment;filename="%s"' % filename  # 邮件附件名
        self.mail.attach(file)  # 添加附件

    def Send(self, server, port, MailUser, MailPwd, To_Addr):
        # 连接邮件
        Send = smtplib.SMTP_SSL(server, port)
        Send.login(MailUser, MailPwd)  # 登录邮箱
        Send.sendmail(MailUser, To_Addr, self.mail.as_string())  # 发送邮件
        Send.quit()  # 退出连接
        print("发送成功")


if __name__ == '__main__':
    sendmail = SendMail()
    sendmail.Add_text('为了联盟', '为了部落', '万厚超', '万厚超')
    sendmail.Send('smtp.qq.com', 465, MailUser, MailPwd, '1154887004@qq.com')
