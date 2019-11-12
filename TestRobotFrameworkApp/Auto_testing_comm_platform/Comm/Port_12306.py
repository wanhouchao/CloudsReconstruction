import time,requests,os,json
from prettytable import PrettyTable

def station_coed(fstation,tstation):
    url ='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js' \
         '?station_version=1.9108'
    r = requests.get(url)
    info =  r.text
    data = info.split('|')
    fcode=''
    tcode=''
    #print(data)
    for i in data:
        if i == fstation :
            fcode = data[data.index(fstation)+1]
        elif i == tstation:
            tcode = data[data.index(tstation) + 1]
    if fcode =='' or tcode == '':
        print('车站不存在')
    else:
        return (fcode,tcode)
def getTicket(fstation,tstation,date):
    fcode,tcode = station_coed(fstation, tstation)
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?' \
          'leftTicketDTO.train_date=%s' \
          '&leftTicketDTO.from_station=%s' \
          '&leftTicketDTO.to_station=%s' \
          '&purpose_codes=ADULT'%(date,fcode,tcode)
    r = requests.get(url)
    info = json.loads(r.text)['data']['result']
    for i in info:
        Table= PrettyTable()
        Table.field_names = (['车次','出发时间','到达时间','历时','商务座',
                                    '一等座','二等座','硬卧','硬座','无座'])
        #-7是商务座 -8一等座 -9二等座 3是车次  8是出发时间 9是到达时间 10是历时 -13是硬卧 -11是硬座 -10是无座
        data = str(i).split('|')
        Table.add_row([data[3],data[8],data[9],data[10],data[-7],data[-8],data[-9],
                       data[-13],data[-11],data[-10]])
        print(Table)
        gettimetable(data[2], fstation, tstation, date)


def gettimetable(num,fstation,tstation,date):
    fcode, tcode = station_coed(fstation, tstation)
    url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?' \
          'train_no=%s' \
          '&from_station_telecode=%s' \
          '&to_station_telecode=%s' \
          '&depart_date=%s'%(num,fcode,tcode,date)
    r = requests.get(url)
    info = json.loads(r.text)['data']['data']
    #print(info)
    Table = PrettyTable()
    Table.field_names =(['站序','站名','到站时间','出发时间','停留时间'])
    for i in info:
        Table.add_row([i['station_no'],i['station_name'],i['arrive_time'],i['start_time'],i['stopover_time']])
    print(Table)



if __name__ == '__main__':
    # fstation = input('请输入起始站：')
    # tstation=input('请输入终点站：')
    # date=input('请输入出入日期：')
    # getTicket(fstation,tstation,date)
    def timestamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
        '''这个是把时间戳转换成格式化好的实际，如果不传时间戳，那么就返回当前的时间'''
        if timestamp:
            return time.strftime(format, time.localtime(timestamp))

        else:
            return time.strftime(format, time.localtime())
    print(timestamp_to_str())

























































