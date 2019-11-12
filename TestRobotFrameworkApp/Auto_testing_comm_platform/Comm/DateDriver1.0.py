import os
import xlrd
import xlwt


class ReadExcel:
    def __init__(self, path):
        '''传excel地址path'''
        try:
            self.data = xlrd.open_workbook(path)  # data--excel数据
        except:
            print("请传入正确的地址！！！")

    def GetSheetsName(self):
        '''获取sheet名字列表'''
        self.tabale_list = self.data.sheet_names()
        return self.tabale_list

    def GetTable(self, string_ele):
        '''传入下标索引index或者表格名字name返回表格数据'''
        if str(string_ele).find('=') == -1:
            raise ('元素的方式错误，无法解析')  # raise手动触发异常
        else:
            method = str(string_ele).split('=')[0]
            ele = str(string_ele).split('=')[1]
            if method == 'index':
                try:
                    self.table = self.data.sheet_by_index(int(ele))
                    return self.table
                except:
                    print('没有找到这个索引的表格！！！')
            elif method == 'name':
                try:
                    self.table = self.data.sheet_by_name(str(ele))
                    return self.table
                except:
                    print('没有找到这个名字的表格！！！')
            else:
                print('格式错误,只能按照index=xxx,name=xxx的格式写入！！！')

    def ReadRowsTable(self, string_ele):
        '''按照表index和name一行一行读取返回读取列表Value_list'''
        try:
            table = self.GetTable(string_ele)
            self.Value_list = []
            for i in range(0, table.nrows):
                self.Value_list.append(table.row_values(i))
            return self.Value_list
        except:
            pass

    def Getdata(self, string_ele):
        '''处理数据'''
        data_list = self.ReadRowsTable(string_ele)
        self.DataTable = {}
        self.DataTable['title'] = data_list[0]
        for i in range(1, len(data_list)):
            self.DataTable['test_case%s' % i] = data_list[i]
        return self.DataTable

