from django.urls import path
from django.urls.resolvers import URLPattern
import delivery

from . import views

from delivery import views
from . import views

app_name = 'member'
urlpatterns = [
    path('list/', views.d_mypage_orderlist, name='d_mypage_orderlist'), 
    path('index/', views.IndexView.as_view(), name='index'),
    path('signup/', views.signup, name="signup"),  # 임의
    path('login/', views.login, name="login"), # 임의
    # path('signup/', views.signup, name='signup'), # 임의

    path('signup/', views.signup, name='signup'), # 임의
    path('logout/', views.logout, name='logout'),
    path('reviewrider/', views.review_rider_view, name="review_rider"),
    path('reviewcustomer/', views.review_cus_view, name="review_customer"),
    path('mypage/', views.mypage_view, name="mypage"),
    # path('register/', delivery.views.register_rider_view, name="register_rider"),

]

