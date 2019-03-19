from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
def index1(request):
    return HttpResponseRedirect('/sunck')
def index(request):
    # 数据操作
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')


def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

#获取get传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a + "  " + b + "  " + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + "  " + a2 + "  " + c)

# POST
def showregist(request):
    return render(request, 'myApp/regist.html')
def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("post")


# response
def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

# cookie
def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["sunck"]+"</h1>")
    # cookie = res.set_cookie("sunck","good")
    return res



# 重定向
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect('/sunck/redirect2')
    return redirect('/sunck/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向后的视图")




# session
def main(request):
    # 去session
    username = request.session.get('name',"游客")
    return render(request, 'myApp/main.html',{'username':username})
def login(request):
    return render(request, 'myApp/login.html')
def showmain(request):
    print("sdfasgadgsdfgsreg")
    username = request.POST.get('username')
    # 存储session
    request.session['name'] = username
    # request.session.set_expiry(10)
    return redirect('/sunck/main/')
from django.contrib.auth import logout
def quit(request):
    # 清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/sunck/main/')




