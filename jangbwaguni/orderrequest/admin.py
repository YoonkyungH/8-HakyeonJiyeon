from django.contrib import admin

from .models import Customer, OrderApply
admin.site.register(Customer)
admin.site.register(OrderApply)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity',)

# admin.site.register(OrderApply, OrderAdmin)

