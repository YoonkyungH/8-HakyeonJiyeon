from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register_rider_view, name="register_rider"),
    path('list/', views.order_list_view, name="order_list"), # 임의
    # path('register/<int:cus_id>', views.register_rider_view, name="register_rider"),
    path('register/', views.register_rider_view, name="register_rider"),


]
