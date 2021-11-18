from django.contrib import admin

from .models import Customer, Rider
from orderrequest.models import OrderApply

# class OrderApplyInline(admin.StackedInline):
#     model = OrderApply # inline으로 보여질 모델의 종류
#     extra = 3 # inline으로 보여질 개수

# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [OrderApplyInline]

# class RiderAdmin(admin.ModelAdmin):
#     inlines = [OrderApplyInline]

# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Customer)
admin.site.register(Rider)
# admin.site.register(OrderApply)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('cus_id', )

# admin.site.register(user, UserAdmin)
