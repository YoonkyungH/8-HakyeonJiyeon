from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'member'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('signup', views.signup, name='signup'),
    path('list/', views.d_mypage_orderlist, name='d_mypage_orderlist'),
    path('reviewrider/', views.review_rider_view, name="review_rider"),
    path('reviewcustomer/', views.review_cus_view, name="review_customer"),
    path('mypage/', views.mypage_view, name="mypage"),
]