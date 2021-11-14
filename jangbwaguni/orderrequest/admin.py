from django.contrib import admin

from .models import orders


# class DeliveryAdmin(admin.ModelAdmin):
#     list_display = ('cus_name', 'order_product', 'cus_address', )

# admin.site.register(orders, DeliveryAdmin)  # 이렇게 하면 admin 목록에서 이름, 주문한 상품, 주소를 나타냄
admin.site.register(orders)
