import requests
import json

# url = 'http://logistics-api-test.epsit.cn:6066/api/robot/telephoneCommand'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#         ,'Content-Type': 'application/x-www-form-urlencoded'}
# data = 'account=demo' \
#        '&password=3f496f37163c35aac60ff68023f639f6&referer=http%3A%2F%2Fdemo.ranzhi.org%2Fsys%2Findex.php&rawPassword=fe01ce2a7fbac8fafaed7c982a04e229&keepLogin=false'
# r = requests.post(url,data,headers=head)

class Requests():
    def Text(self,way,url,data):
        if way == 'get':
            self.r = requests.get(url, data)
            return self.r
        elif way == 'post':
            self.r = requests.post(url, data)
            return self.r
        else:
            print('兄弟不要瞎玩！！！')
if __name__ == '__main__':
    # url = 'http://logistics-api-test.epsit.cn:6066/api/auth/robotLogin'
    # data = {"account": "yunji01", "password": "MTIzNDU2"}
    # r = Requests()
    # data_ = r.Text('post',url,data)
    # print(data_)
    url_ = 'http://127.0.0.1:8000/msggate/'
    # data_ = {"csrfmiddlewaretoken":"7997cylxZCmXELOizqybB7bD3pm3McPXI6wEq5eY5J9lnJ8oM0PSxQzejXuuYIBr","userA":"首领","userB":"兽人","msg":"你好1"}
    data_= {"userC":"黄蓉"}
    head_ = {"Content-Type":"text/html; charset=utf-8"}
    r = requests.get(url_)
    print(r.reason)