from django.urls import path
from .import views

    

urlpatterns = [
    
    path("",views.index,name="index"),
    path('about_us',views.about_us,name='about_us'),
    path('our_service',views.our_service,name='our_service'),
    path("show_product",views.show_product,name='show_product'),
    path('search_product',views.search_product,name="search_product"),

]
