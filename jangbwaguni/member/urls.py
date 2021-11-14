from django.urls import path
# from django.urls.resolvers import URLPattern
from . import views


# urlpatterns = [
#     path('signup', views.signup, name='signup'),
#     # path('login', views.Login, name = 'login'),
# ]

app_name = 'member'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.login, name="login"),
]