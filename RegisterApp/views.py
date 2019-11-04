from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from requests import Response


def register(request):
    return render(request, 'register.html')


def RegisterSubmit(request):
    if request.method == 'POST':
        registerUsername = request.POST.get('registerUsername', None)
        registerPassword = request.POST.get('registerPassword', None)
        # VerifyPassword=request.POST.get('VerifyPassword', None)
        registerEmail = request.POST.get('registerEmail', None)
        with open("UserInfo.txt", 'a+') as f:
            data = "|{}|{}|{}|@".format(registerUsername, registerPassword, registerEmail)
            f.write(data)
            f.close()
    # return HttpResponse("<a href='http://47.98.58.33:8000'>注册成功,点击返回登录</a>")
        return HttpResponse("<script>alert('注册成功！');window.location='http://127.0.0.1:8000';</script>")



if __name__ == "__main__":
    while 1:
        registerUsername = input("1:")
        registerPassword = input("2:")
        # VerifyPassword=request.POST.get('VerifyPassword', None)
        registerEmail = input("3:")
        data = "|{}|{}|{}|@".format(registerUsername, registerPassword, registerEmail)
        # with open("UserInfo.txt", 'a+') as f:
        #     data = "|{}|{}|{}|@".format(registerUsername, registerPassword, registerEmail)
        #     f.write(data)
        #     f.close()
        print(data)
