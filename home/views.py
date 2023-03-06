from django.shortcuts import render,redirect
from .models import categories,items,add_cart
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from accounts.models import *
from django.db.models import Sum ,F

category = categories.objects.all().order_by('?')
cart = add_cart.objects.all()
def index(request):
    try:
        user = User.objects.get(username=request.user.username)
        count = add_cart.objects.filter(user = user).count()
        like =  wishlist.objects.filter(user=user)
    except:
        count = None
        like = None
    item = items.objects.all()
    return render(request,"index.html",
    {
        'cat' : category,
        'food_items' : item,
        'cart_count' :   count,
        'like' : like ,
    })

def about_us(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        count = add_cart.objects.filter(user = user).count()
        return render(request,"about_us.html",
        { 
        'cart_count' : count,

        })
    else:
        return render(request,"about_us.html")

def our_service(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        count = add_cart.objects.filter(user = user).count()
        return render(request, 'our_services.html',
        { 
        'cart_count' : count,

        })
    else:
        return render(request, 'our_services.html')

def show_product(request):
        if request.method == 'GET':
            product_id = request.GET['item']
            item = items.objects.all().order_by('?')
            check =product_id.split("-")
            if request.user.is_authenticated:
                user_id = User.objects.get(username=request.user.username)
                count = add_cart.objects.filter(user = user_id).count()
                if check[0] == "category":
                    return render(request, "cat_items.html",{'cat_items' : item, 'category_name': check[1] })
                else:
                    verify = None
                    like = wishlist.objects.filter(user=user_id)
                    if add_cart.objects.filter(item_name= product_id, user= user_id).exists():
                            verify = True
                    return render(request, 'open_item.html',{'open_items' :item ,'id' : product_id, 'cart_count' : count , 'check' : verify ,"like": like })
            else:
                if check[0] == "category":
                    return render(request, "cat_items.html",{'cat_items' : item, 'category_name': check[1] })
                else:                                
                    return render(request, 'open_item.html',{'open_items' :item ,'id' : product_id })
        else:
            return redirect(request.META['HTTP_REFERER'])


def search_product(request):
    if request.method == 'GET':
        get = request.GET['query']
        get = get.title()
        data = items.objects.all()
        if request.user.is_authenticated:
                user_id = User.objects.get(username=request.user.username)
                count = add_cart.objects.filter(user = user_id).count()
                return render(request, "search.html",{'data' : data, 'get': get , 'cart_count' : count })
        else:
            return render(request, "search.html",{'data' : data, 'get': get , })

    else:
        return redirect(request.META['HTTP_REFERER'])