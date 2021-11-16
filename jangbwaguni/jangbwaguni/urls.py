from django.contrib import admin
from django.urls import path, include

# 정적파일 제공

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main/', include('main.urls')),
    path('delivery/', include('delivery.urls')),
    path('order/', include('orderrequest.urls')),
    path('mypage/', include('member.urls')),
] 

urlpatterns += \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
