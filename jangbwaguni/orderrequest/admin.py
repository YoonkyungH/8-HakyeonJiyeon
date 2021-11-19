from django.contrib import admin

from .models import OrderApply, EvalRider, EvalCustomer

admin.site.register(OrderApply)
admin.site.register(EvalRider)
admin.site.register(EvalCustomer)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity',)

# admin.site.register(OrderApply, OrderAdmin)

