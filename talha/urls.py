"""talha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from app import views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.result,name="main"),
    path('<slug>', views.product_details),
    path('account/',views.my_account,name="account"),
    path('add_cart/<int:id>',views.add_cart,name="add_cart"),
    path('remove_cart/<int:id>',views.remove_cart,name="remove_cart"),
    
    path('login_user/', views.my_login,name="login_user"),
    path('logout_user/', views.my_logout),
    path('cart_user/', views.my_cart,name="cart_user/"),
    path('cart_user_inc/<int:id>', views.item_increment,name="cart_user_inc"),
    path('cart_user_dec/<int:id>/', views.item_decrement,name="cart_user_dec"),
    path('cart_clear/', views.cart_clear,name="cart_clear"),
    path('check_user/', views.Check_user,name="check_user"),
    path('add_user/', views.Add_user,name="add_user"),
    path('check_out/', views.check_out,name="check_out/"),
    
    path('ckeditor', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
