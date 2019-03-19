from django.shortcuts import render
from .models import Wheel,Nav,Mustbuy,Shop,MainShow
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



def market(request):
    return render(request, 'axf/market.html', {"title":"闪送超市"})

def cart(request):
    return render(request, 'axf/cart.html', {"title":"购物车"})

def mine(request):
    return render(request, 'axf/mine.html', {"title":"我的"})

