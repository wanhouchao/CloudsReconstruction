import os
import xlrd
import xlwt


class Excel:
    def __init__(self, Path):
        '''传入文件地址，判断文件地址是否存在'''
        if os.path.exists(Path):
            try:
                self.data = xlrd.open_workbook(Path)  # 读取文件数据
                self.tabale_list = self.data.sheet_names()
            except:
                raise print("这个地址不是一个excle文件！！！\n")
        else:
            raise print("地址不存在！！！\n")

    def GetTable(self,IndexOrName,way=1):
        '''传入下标索引index或者表格名字name返回表格数据,默认按照名字传入'''
        if way == 1 :
            try:
                self.table = self.data.sheet_by_name(IndexOrName)
                return self.table
            except:
                raise print('没有找到这个名字的表格！！！\n')
        elif way == 2:
            try:
                self.table = self.data.sheet_by_index(IndexOrName)
                return self.table
            except:
                raise print('没有找到这个索引的表格！！！\n')
        else:
            raise print("没有这样的方法\n")

    def  ReadRowsTable(self, IndexOrName,way=1):
        '''按照表index和name一行一行读取返回读取列表Value_list'''
        table = self.GetTable(IndexOrName,way=way)
        self.Value_list = []
        for i in range(0, table.nrows):
            self.Value_list.append(table.row_values(i))
        return self.Value_list

    def DataUp(self, IndexOrName,way=1):
        '''提取除数据标题栏和数据栏'''
        DataALL = self.ReadRowsTable(IndexOrName,way=way)
        Data = {'title':DataALL[0],'data':DataALL[1:]}
        return Data




if __name__ == "__main__":
    path = 'test.xls'
    Data= Excel(path).DataUp('Sheet1')
    print(Data)
