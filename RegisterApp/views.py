from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html')

def RegisterSubmit(request):
    cut = False
    if request.method =='POST':
        user =request.POST.get('user', None)
        password=request.POST.get('password', None)
        # VerifyPassword=request.POST.get('VerifyPassword', None)
        mail=request.POST.get('mail', None)
        phone=request.POST.get('phone', None)
        if len(user)!=0 and password != 0:
            with open("UserInfo.txt",'a+') as f:
                data="|{}|{}|{}|{}|@".format(user,password,mail,phone)
                f.write(data)
                f.close()
            cut =True
    if cut:
        return HttpResponse('注册成功\n' + '<a href="http://127.0.0.1:8000">点击跳转到首页</a>')
    else:
        return HttpResponse('兄弟别瞎玩，注册不成功\n' + '<a href="http://127.0.0.1:8000/register/">点击跳转到注册页面</a>')
