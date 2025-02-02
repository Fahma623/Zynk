from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('shop/', views.shop, name='shop'),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('chat/', views.chat, name='chat'),
]
