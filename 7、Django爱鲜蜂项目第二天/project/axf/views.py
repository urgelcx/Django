from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User
# Create your views here.

def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()

    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()


    return render(request, 'axf/home.html', {"title":"主页","wheelsList":wheelsList,"navList":navList,"mustbuyList":mustbuyList,"shop1":shop1,"shop2":shop2,"shop3":shop3,"shop4":shop4,"mainList":mainList})



def market(request, categoryid, cid, sortid):
    leftSlider = FoodTypes.objects.all()

    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        productList = Goods.objects.filter(categoryid=categoryid,childcid = cid)

    # 排序
    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")

    group = leftSlider.get(typeid = categoryid)
    childList = []
    # 全部分类:0#进口水果:103534#国产水果:103533
    childnames = group.childtypenames
    arr1 = childnames.split("#")
    for str in arr1:
        # 全部分类:0
        arr2 = str.split(":")
        obj = {"childName":arr2[0],"childId":arr2[1]}
        childList.append(obj)



    return render(request, 'axf/market.html', {"title":"闪送超市","leftSlider":leftSlider,"productList":productList,"childList":childList,"categoryid":categoryid,"cid":cid})

def cart(request):
    return render(request, 'axf/cart.html', {"title":"购物车"})




def mine(request):
    return render(request, 'axf/mine.html', {"title":"我的"})
# 登陆
from .forms.login import LoginForm
from django.http import HttpResponse
def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            # 信息格式没多大问题，验证账号和密码的正确性
            print("***************")
            name = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]


            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {"title": "登陆", "form": f,"error":f.errors})
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {"title": "登陆","form":f})


#注册
def register(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'axf/register.html', {"title":"注册"})

#

def checkuserid(request):
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount = userid)
        return JsonResponse({"data":"改用户已经被注册","status":"error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})


