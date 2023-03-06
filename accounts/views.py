from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import *
from home.models import *
from django.db.models import Sum ,F
import secrets

def login(request):
    return render(request ,'login.html')

def signup(request):
    return render(request ,'signup.html')

def profile(request):
    user = User.objects.get(username=request.user.username)
    count = add_cart.objects.filter(user = user).count()
    if profile_data.objects.filter(email= user).exists():
        data = profile_data.objects.all()
        return render(request ,'profile.html',
        { 
        'profile_info' : data ,
        'cart_count' : count,

        })
    else:
        return render(request ,'profile_create.html',{'cart_count' : count})


def yummy_signup(request):  

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password :

            if User.objects.filter(username = email).exists(): 
                messages.error(request,"Email already taken")
                return redirect('signup')


            else:
                new_user = User.objects.create_user( username = email , password = password)
                new_user.save()
                messages.success(request,"SignUp Is Successful")
                return redirect('login')

        else:   
            messages.error(request,"Password Not Matched")
            return redirect('signup')

    else:
        messages.error(request,'Something Went Wrong')
        return redirect('signup')

def yummy_login(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(username = email , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    else:
        messages.error(request,'Something Went Wrong')
        return redirect('login')



def logout(request):
    auth.logout(request)
    return redirect('/')


def profile_create(request):
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        create = profile_data.objects.create( first_name = first_name , last_name= last_name,phone= phone , email=email, address= address)
        create.save()
        messages.success(request,"Successfully Updated")
        return redirect('profile')
    else:
        messages.error(request, "Something Went Wrong")
        return redirect('profile')

def profile_update(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']

        update = profile_data.objects.filter(email= email).update(first_name=first_name,last_name=last_name,phone=phone,address=address)
        messages.success(request,"Successfully Updated")
        return redirect('profile')
    else:
        messages.error(request, "Something Went Wrong")
        return redirect('profile')



def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_item = request.POST['item']
            user_name = request.POST['user_id']
            table1_rows = items.objects.filter(item_name= add_item)
            for row in table1_rows.values():
                add_cart.objects.create(**row)
                add_cart.objects.filter(item_name= add_item,user= "none").update(user = user_name)
            user = User.objects.get(username=request.user.username)
            count = add_cart.objects.filter(user = user).count()
            messages.success(request, "Added to cart")
            return redirect(request.META['HTTP_REFERER'])   

        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, "Please Login to Add to Cart")
        return redirect(request.META['HTTP_REFERER'])


def cart(request):
        data = profile_data.objects.all()
        shipping = profile_data.objects.all()
        items_in_cart = add_cart.objects.all()
        user = User.objects.get(username=request.user.username)
        count = add_cart.objects.filter(user = user).count()
        mul = add_cart.objects.filter(user = user).extra(select={'mul': 'item_price * quantity'})
        add = add_cart.objects.filter(user = user).aggregate(add=Sum(F('item_price')*F('quantity')))['add']
        return render(request, 'cart.html',
        {
        "cart" : items_in_cart, 
        'cart_count' : count,
        'profile_info' : data ,
        'total': mul,
        'add' : add,
        'shipping' : shipping

        })

def buy(request):
    if request.user.is_authenticated:
        shipping = profile_data.objects.all()
        temp_data = temp_cart.objects.all()
        data = profile_data.objects.all()
        if request.method == 'GET':
            add_item = request.GET['item']
            user_name = request.GET['user_id']
            count = add_cart.objects.filter(user = user_name).count()
            if temp_cart.objects.filter(user=user_name,item_name= add_item).exists():
                mul = temp_cart.objects.filter(user = user_name , item_name= add_item).extra(select={'mul': 'item_price * quantity'})
                add = temp_cart.objects.filter(user = user_name, item_name=add_item).aggregate(add=Sum(F('item_price')*F('quantity')))['add']
                return render(request, 'buy_now.html',{
                'cart' : temp_data,
                'cart_count' : count,
                'profile_info' : data ,
                'total': mul,
                'add' : add,
                'requested_item': add_item,
                'shipping': shipping})   
            else:   
                table1_rows = items.objects.filter(item_name= add_item)
                for row in table1_rows.values():
                    temp_cart.objects.create(**row)
                    temp_cart.objects.filter(item_name= add_item,user= "none").update(user = user_name)
                    mul = temp_cart.objects.filter(user = user_name , item_name= add_item).extra(select={'mul': 'item_price * quantity'})
                add = temp_cart.objects.filter(user = user_name, item_name=add_item).aggregate(add=Sum(F('item_price')*F('quantity')))['add']
                return render(request, 'buy_now.html',{
                'cart' : temp_data,
                'cart_count' : count,
                'profile_info' : data ,
                'total': mul,
                'add' : add,
                'requested_item': add_item,
                'shipping': shipping})   

        else:
            return redirect(request.META['HTTP_REFERER'])
            
    else:
        messages.error(request, "Please Login to Buy")
        return redirect(request.META['HTTP_REFERER'])   

def update_cart(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        user = User.objects.get(username=request.user.username)
        add_cart.objects.filter(item_name= item_name , user=user).update(quantity=quantity)
        messages.success(request, "Updated")
        return redirect(request.META['HTTP_REFERER'])

    else:
        return redirect(request.META['HTTP_REFERER'])

def tempt_update_cart(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        user = User.objects.get(username=request.user.username)
        temp_cart.objects.filter(item_name= item_name ,user=user).update(quantity=quantity)
        messages.success(request, "Updated")
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def remove_from_cart(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        user = User.objects.get(username=request.user.username)
        remove = add_cart.objects.filter(item_name= item_name , user=user)
        remove.delete()
        messages.success(request, "Removed from cart")
        return redirect(request.META['HTTP_REFERER'])


def shipping_address(request):
    if request.user.is_authenticated:
        shipping = profile_data.objects.all()
        user = User.objects.get(username=request.user.username)
        count = add_cart.objects.filter(user = user).count()
        if request.method == "POST":
            address = request.POST['address']
            user = request.POST['username']
            if profile_data.objects.filter(email= user).exists():
                if profile_data.objects.filter(email= user,shipping_address_1= "none"):
                    profile_data.objects.filter(email= user).update(shipping_address_1=address)
                    messages.success(request, "Successfully Added")
                    return redirect(request.META['HTTP_REFERER'])
                elif profile_data.objects.filter(email= user,shipping_address_2= "none"):
                    profile_data.objects.filter(email= user).update(shipping_address_2=address)
                    messages.success(request, "Successfully Added")
                    return redirect(request.META['HTTP_REFERER'])
                elif profile_data.objects.filter(email= user,shipping_address_3= "none"):
                    profile_data.objects.filter(email= user).update(shipping_address_3=address)
                    messages.success(request, "Successfully Added")
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    messages.error(request, "Up to 3 Shipping Address are allowed")
                    return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, "Please Update Profile")
                return redirect(request.META['HTTP_REFERER'])
        else:
            return render(request, 'shipping_address.html',{'shipping' : shipping,'cart_count' : count,})
    else:
        return redirect(request.META['HTTP_REFERER'])


def set_default(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            address = request.POST['set']
            user = request.POST['username']
            profile_data.objects.filter(email= user).update(default_shipping_address=address)
            messages.success(request, "Default Address set successful")
            return redirect(request.META['HTTP_REFERER'])
        else:
                return redirect(request.META['HTTP_REFERER'])
    else:
                return redirect(request.META['HTTP_REFERER'])


def delete_address(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            address = request.POST['set']
            user = User.objects.get(username=request.user.username)
            if profile_data.objects.filter(email= user , shipping_address_1= address).exists():
                profile_data.objects.filter(email= user , shipping_address_1= address).update(shipping_address_1= "none")
                messages.success(request, "Deleted successful")
                return redirect(request.META['HTTP_REFERER'])
            elif profile_data.objects.filter(email= user , shipping_address_2= address).exists():
                profile_data.objects.filter(email= user , shipping_address_2= address).update(shipping_address_2= "none")
                messages.success(request, "Deleted successful")
                return redirect(request.META['HTTP_REFERER'])
            else:
                profile_data.objects.filter(email= user , shipping_address_3= address).update(shipping_address_3= "none")
                messages.success(request, "Deleted successful")
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


# def edit_address(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             try:
#                 address_1 = request.POST['address_1']
#                 address_2 = request.POST['address_2']
#                 address_3 = request.POST['address_3']
#                 user = User.objects.get(username=request.user.username)
#                 profile_data.objects.filter(email= user).update(shipping_address_1= address_1 , shipping_address_2= address_2 , shipping_address_3= address_3)
#                 messages.success(request, "Edited Successfully")
#                 return redirect(request.META['HTTP_REFERER'])
#             except:
#                 address_2 = request.POST['address_2']
#                 address_3 = request.POST['address_3']
#                 user = User.objects.get(username=request.user.username)
#                 profile_data.objects.filter(email= user).update(shipping_address_2= address_2 , shipping_address_3= address_3)
#                 messages.success(request, "Edited Successfully")
#                 return redirect(request.META['HTTP_REFERER'])
            
#         else:
#             return redirect(request.META['HTTP_REFERER'])
#     else:
#         return redirect(request.META['HTTP_REFERER'])

def cart_to_buy(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        table1_rows = add_cart.objects.filter(user= user)
        for row in table1_rows.values():
            order_cart.objects.create(**row)
        records = profile_data.objects.filter(email=user)
        first_column = records.first()
        update_shipping_address = first_column.default_shipping_address
        update_total_price = order_cart.objects.filter(user = user,).aggregate(add=Sum(F('item_price')*F('quantity')))['add']
        update_order_id = secrets.token_hex(8)
        order_cart.objects.filter(user=user).update(shipping_address=update_shipping_address,payment_id= 4,total_price=update_total_price,order_id=update_order_id,status="Confirmed",tracking="Ordered")
        remove_from_cart = add_cart.objects.filter(user=user)
        remove_from_cart.delete()
        messages.success(request, "Order is Successful")
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.success(request, "Something went wrong")
        return redirect(request.META['HTTP_REFERER'])

def orders(request):
    user  = User.objects.get(username=request.user.username)
    count = add_cart.objects.filter(user = user).count()
    get_order = order_cart.objects.all()
    return render(request, 'order.html',{'cart_count' : count,'get_order':get_order})


def buy_to_buy(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            item_name = request.POST['item_name']
            user = User.objects.get(username=request.user.username)
            table1_rows = temp_cart.objects.filter(user= user,item_name=item_name)
            for row in table1_rows.values():
                order_cart.objects.create(**row)
            records = profile_data.objects.filter(email=user)
            first_column = records.first()
            update_shipping_address = first_column.default_shipping_address
            update_total_price = order_cart.objects.filter(user = user,).aggregate(add=Sum(F('item_price')*F('quantity')))['add']
            update_order_id = secrets.token_hex(8)
            order_cart.objects.filter(user= user,item_name=item_name,shipping_address="none",payment_id=0,total_price=0,order_id="none",status="none",tracking="none").update(shipping_address=update_shipping_address,payment_id= 4,total_price=update_total_price,order_id=update_order_id,status="Confirmed",tracking="Ordered")
            remove_from_cart = temp_cart.objects.filter(user=user)
            remove_from_cart.delete()
            messages.success(request, "Order is Successful")
            return redirect('/accounts/orders')
    else:
        messages.error(request, "Something went wrong")
        return redirect(request.META['HTTP_REFERER'])

def cancel_order(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method =='POST':
            item_name = request.POST['item_name']
            order_id = request.POST['order_id']
            cancel_order = order_cart.objects.filter(user=user,item_name=item_name,order_id=order_id)
            cancel_order.delete()
            messages.success(request, "Order Successfully Canceled ")
            return redirect('/accounts/orders')
        messages.error(request, "Something went wrong")
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, "Something went wrong")
        return redirect(request.META['HTTP_REFERER'])

def like(request):
    if request.user.is_authenticated:
            item_name = request.GET.get('item_name')
            values=item_name.split("and")
            print(values[-1])
            table1_rows =items.objects.filter(item_name=values[0])
            for row in table1_rows.values():
                wishlist.objects.create(**row)
            wishlist.objects.filter(item_name=values[0],user="none").update(like="True",user=values[-1])
            wishlist.objects.filter(item_name=values[0],user="none").update(like="True",user=values[-1]) 
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def dis_like(request, item_name):
    if request.user.is_authenticated:
        if request.method == 'POST':
            item = item_name
            user = username
            remove = wishlist.objects.filter(item_name=item_name,user=user)
            remove.delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])