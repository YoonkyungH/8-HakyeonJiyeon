"""jangbwaguni URL Configuration

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
from django.urls import path, include
# from member.views import CreateUser, Login
from member import views as m


from member.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', m.index),
    path('register/', m.RegisterView.as_view()),  # class 사용하는 경우 as_view 사용
    path('login/', m.LoginView.as_view()),
    path('logout/', m.LogoutView.as_view()),
    # path('login/', m.views.login, name='login'),
    
    
    # path('member/signup', m.signup, name='signup'),
    # path('member/login', login_view, name = "login"),
    # path('member/logout', logout_view, name = "logout"),


    # path('logout/', m.views.logout, name='logout'),
]
