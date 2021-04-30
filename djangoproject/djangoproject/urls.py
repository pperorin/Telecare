"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blogs import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),            #หน้าหลัก
    path('addForm',views.addForm),      #จอง
    path('',views.signin),              #login
    path('signin',views.signin),     
    path('signup',views.signup),        #register
    path('check',views.check),          
    path('personnel',views.personnel),  #ของหมอ
    path('userInformation',views.userInformation),
    path('disease',views.disease),
    path('about',views.about),


]
