from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# 정적파일 제공
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'orderrequest'
urlpatterns = [
     path('customer/<int:rider_id>/', views.d_order_cus, name='d_order_cus'),
    path('rider/', views.d_rider_list, name='d_rider_list'),
    # path('customer/<int:cus_id>/<int:rider_id>/', views.d_order_cus, name='d_order_cus'),
    # path('rider/<int:cus_id>/', views.d_rider_list, name='d_rider_list'),
    # path('rider/', views.IndexView.as_view(), name='index'),
]

urlpatterns += \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
