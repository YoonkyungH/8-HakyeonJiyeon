from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('customer/', views.d_order_cus, name='d_order_cus'),
    path('rider/', views.d_rider_list, name='d_rider_list'),
]