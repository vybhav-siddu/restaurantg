"""restaurant URL Configuration

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
from django.urls import path, include
from restaurant import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/customers/', views.customer_list),
    path('customers/', views.customer_list),
    path('customers/<int:id>', views.customer_detail),
    path('dishs/', views.dish_list),
    path('dishs/<int:id>', views.dish_detail),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail),
    path('orders/', views.order_list),
    path('orders/<int:id>', views.order_detail),
    path('workers/', views.worker_list),
    path('workers/<int:id>', views.worker_detail),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)