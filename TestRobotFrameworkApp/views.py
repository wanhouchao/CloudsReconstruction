from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def CreateCase(request):
    return render(request, 'CreateCase.html')


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


def CreateCode(request):
    Creator = request.POST.get('Creator', None)
    ModuleName = request.POST.get('ModuleName', None)
    CaseName = request.POST.get('CaseName', None)
    Assert = request.POST.get('assert', None)
    ExpectedResult = request.POST.get('ExpectedResult', None)
    ActualResult = request.POST.get('ActualResult', None)
    URL = request.POST.get('URL', None)
    action = request.POST.getlist('action', None)  # Django获取相同的name属性值
    elements = request.POST.getlist('elements', None)
    print("{}--{}--{}--{}--{}--{}--{}--{}--{}".format(Creator,ModuleName,CaseName,Assert,ExpectedResult,ActualResult,URL,action,elements))
    return HttpResponse("<script>alert('创建成功！');window.location='http://127.0.0.1:8000/CreateCase/';</script>")


if __name__ == "__main__":
    string = '万厚超--后台--登录--assertNotEqual--200--200--www.baidu.com--Click--//*[@id="action_0"]2'
    list= string.split('--')
    print(list)
