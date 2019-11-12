import os, time
from Auto_testing_comm_platform.Comm.SeleniumFramework import *
from Auto_testing_comm_platform.Config.test_epsit import *


def Read(path, switch='read', enc='utf-8'):
    """
    读取文件数据
    path : 文件地址
    switch: 键值开关，默认格式化读取，switch=readlines一行一行读
    add_text: 添加的内容
    enc: 编码模式，默认utf-8
    return: 文件内容
    """
    f = open(path, 'r', encoding=enc)
    if switch == 'read':
        data = f.read()
        f.close()
        return data
    elif switch == 'readlines':
        data = f.readlines()
        f.close()
        return data
    else:
        return print("兄弟switch只能填readlines或者read\n")  #


# 写入文件信息函数，传入文件地址、增加的信息、开关'w'(覆盖写入)'a'(追加写入)，返回文件内容
def Write(path, add_text, switch='w'):
    '''
        写入数据
    path : 文件地址
    switch: 键值开关，默认覆盖写，switch=a追加写
    add_text: 添加的内容
    enc: 编码模式
    return: 文件内容
    '''
    f = open(path, switch, encoding='utf-8')
    if switch == 'a' or switch == 'w':
        data = f.write(add_text)
        f.close()
        return data
    else:
        return print("兄弟switch只能填'a'或者'w'\n")


# 修改文件信息，传入文件地址、需要修改信息的id或者name,返回文件内容
def Revise(path, id_name, enc='utf-8'):
    """
    修改信息
    :param path: 文件夹地址
    :param id_name: 修改人的id或者name
    :param enc: 编码模式
    """
    while 1:
        data = Read(path, 'read')
        data = data.split("@")
        for i in range(0, len(data) - 1):
            data_change = data[i].split("|")
            # print(data_change)
            if data_change[0] == id_name or data_change[1] == id_name:
                option = input("==1修改名字==2修改年龄==3修改性别==4修改薪资==5修改密码\n")
                revise_text = input("请输入修改后的值：")
                data_change[int(option)] = revise_text
            data[i] = str(data_change[0]) + '|' + str(data_change[1]) + '|' + str(data_change[2]) + '|' + str(
                data_change[3]) \
                      + '|' + str(data_change[4]) + '|' + str(data_change[5]) + '@'
        for i in range(0, len(data)):
            if i == 0:
                f = open(path, 'w', encoding='utf-8')
                f.write(str(data[i]))
                f.close()
            else:
                f = open(path, 'a', encoding='utf-8')
                f.write(str(data[i]))
                f.close()
        return Read(path, 'read')


# 查询choose=2,3,精确查询、choose=4模糊查询
# 查询开关默认accuracy精确查找，输入vague模糊查询 返回符合的下标
def Find(pata, id_name, switch="accuracy"):
    '''
    查询函数
    :param pata:文件地址
    :param id_name:查询条件id或者neme
    :param switch: 查询开关默认accuracy精确查找，输入vague模糊查询
    :return:符合要求的下标
    '''
    data = Read(pata, 'readlines')
    data = data[0].split("@")
    index = []
    count = 0
    for i in range(0, len(data) - 1):
        data_info = data[i].split("|")
        if switch == 'accuracy':
            if data_info[0] == id_name or data_info[1] == id_name:
                index.append(i)
                count = 1
                break
        elif switch == 'vague':
            if data_info[0].find(id_name) != -1 or data_info[1].find(id_name) != -1:
                index.append(i)
                count += 1
        else:
            print("兄弟只能输入vague或者accuracy")
    if count == 0:
        print("查不到这个人")
    return index


# 解析payth文件，返回这样的列表[[id,name,...],[],[]...]
def Analyze_text(path):
    """
    解析payth文件，返回这样的列表[[id,name,...],[],[]...]
    :param path:文件地址
    :return:Data返回这样的列表[[id,name,...],[],[]...]
    """
    Data = []
    data = Read(path, 'readlines')
    data = data[0].split("@")
    for i in range(0, len(data) - 1):
        data_ = data[i].split("|")
        Data.append(data_)
    return Data


def Clear_environment():
    '''清理测试环境'''
    os.system("taskkill /f /im chrome* >nul 2>nul")
    os.system("taskkill /f /im gecko* >nul 2>nul")
    os.system("taskkill /f /im ie* >nul 2>nul")


def CutList(list, ElementNumber):
    '''大列表中几个数据组成一个小列表'''
    data = [list[i:i + ElementNumber] for i in range(0, len(list), ElementNumber)]
    return data


def FormatOutput(list):
    '''把列表中元素格式化'''
    pass


def TimeTranslate(Time):
    '''
    可以把格式话时间转化为时间戳
    :param Time: 传入格式化的时间
    :return: 时间戳样式的时间
    '''
    try:
        timeArray = time.strptime(Time, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        return timestamp
    except:
        print('传入的时间格式不正确，需要“%Y-%m-%d %H:%M:%S”格式')
        raise  # 手动触发异常停止程序


if __name__ == '__main__':
    pass
