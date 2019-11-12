from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from TestRobotFrameworkApp.Auto_testing_comm_platform.Comm.SeleniumFramework import SeleniumFramework
from time import sleep

def test(request):
    return render(request, 'test.html')


"""
csrfmiddlewaretoken: zgfV9vHMRIzB0akjKtuFw3k4yuwzWUuBadCsn2AdXPmZJ8EpX3LmsMIFO2E08qg5
Creator: 
ModuleName: 
CaseName: 
assert: assertEqual
ExpectedResult: 
ActualResult: 
browser: Chrome
URL: 
action: Click   
elements: 
"""


def file(request):
    #上传文件
    file=request.FILES.get("fileName")
    print(type(file))
    return HttpResponse("<script>alert('创建成功！')</script>")


if __name__ == "__main__":
    string = '万厚超--后台--登录--assertNotEqual--200--200--https://www.baidu.com/--Click--//*[@id="kw"]'
    list = string.split("--")
    br =SeleniumFramework()
    br.Open_url(list[6])
    if string[7] == 'Click':
        br.Click(list[8])
    else:
        print("输入不对")
    sleep(5)
    br.Out()
