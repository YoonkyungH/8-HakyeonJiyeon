from django.urls import path
from . import views

urlpatterns = [
    path('reviewrider/', views.review_rider_view, name="review_rider"),
    path('reviewcustomer/', views.review_cus_view, name="review_customer"),
    path('mypage/', views.mypage_view, name="mypage"),
]
