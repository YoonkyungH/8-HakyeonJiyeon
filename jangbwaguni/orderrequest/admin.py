from django.contrib import admin

from .models import OrderApply
admin.site.register(OrderApply)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity',)

# admin.site.register(OrderApply, OrderAdmin)

