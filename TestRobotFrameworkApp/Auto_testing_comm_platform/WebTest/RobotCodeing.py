from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from location.Auto_testing_comm_platform.Comm.DateDriver import ReadExcel

'''
输入元素(id、name、xpath、text、css、class)-->elestring
指定行为(web:Click、Write、Clear、Text_up)-->action
生成代码
'''
def robot():
    data = ReadExcel("RobotCodeData.xls").ReadRowsTable("name=Sheet1")
    print(data)
    br = SeleniumFramework()
    br.Open_url('https://www.baidu.com/')
    for i in data:
        elestring = i[0]
        staing = i[1]
        action = i[2]
        if action == 'write':
            br.Write(elestring, staing)
        elif action == 'click':
            br.Click(elestring)
        elif action == 'clear':
            br.Clear(elestring)
        elif action == 'text_up':
            br.Text_up(elestring)
        else:
            print("其他行为暂时没有做出来，敬请期待！！！")
    br.Out()

if __name__=="__main__":
    robot()
