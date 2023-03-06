from django.urls import path
from .import views

urlpatterns = [
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("yummy_signup",views.yummy_signup,name="yummy_signup"),
    path("yummy_login",views.yummy_login,name="yummy_login"),
    path('profile',views.profile,name='profile'),
    path('profile_update',views.profile_update,name="profile_update"),
    path('profile_create',views.profile_create,name="profile_create"),
    path('orders',views.orders,name='orders'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('update_cart',views.update_cart,name="update_cart"),
    path('remove_from_cart',views.remove_from_cart,name='remove_from_cart'),
    path('buy',views.buy,name='buy'),
    path('tempt_update_cart',views.tempt_update_cart,name='tempt_update_cart'),
    path('shipping_address',views.shipping_address,name='shipping_address'),
    path('set_default', views.set_default,name='set_default'),
    path('delete_address',views.delete_address,name="delete_address"),
    # path('edit_address',views.edit_address,name="edit_address"),
    path('cart_to_buy',views.cart_to_buy,name='cart_to_buy'),
    path('buy_to_buy',views.buy_to_buy,name='buy_to_buy'),
    path('cancel_order',views.cancel_order,name='cancel_order'),
    # path('like',views.like,name='like'),
    # path('dis_like',views.dis_like,name='dis_like')

]
 